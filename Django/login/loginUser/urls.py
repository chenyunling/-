
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add/',views.add,name='add'),
    path('detail/<int:userid>',views.detail,name='detail'),
    path('update/<int:userid>', views.update, name='update'),
    path('updateOK/', views.updateOK,name='updateOK'),
]