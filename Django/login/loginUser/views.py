from django.shortcuts import render
from .models import Users

def updateOK(requset):
    tips = ''
    if requset.method == 'POST':
        username = requset.POST.get('username')
        password = requset.POST.get('password')
        user = Users.objects.filter(username=username).first()
        user.password = password
        user.save()
        tips = '更新成功！'
    return render(requset, 'update.html', {'user':user, 'tips':tips})

def update(request, userid):
    user = Users.objects.filter(pk=userid).first()
    return render(request, 'update.html',{'user':user})

# Create your views here.
def index(request):
    users = Users.objects.all()
    return render(request, 'index.html',{'users':users})


def add(request):
    tips = '请填写下面的内容'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        rs = Users.objects.filter(username=username).first()
        if rs:
            tips = '账号已存在，不要重复'
        else:
            Users.objects.create(username=username, password=password)
            tips='添加成功！'


    return render(request, 'add.html', {'tips': tips}) 


def detail(request,userid):
    users = Users.objects.filter(pk=userid).first()

    return render(request,'detail.html',{'user':users})

