
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
	 path('',views.home , name='home'),
	 path('mainhome/',views.mainhome),
	 path('todo/',views.todo,name='todo'),
	 path('updatetask/<str:pk>',views.update ,name= 'updatetask'),
	 path('delete/<str:pk>', views.delete , name='deletetask')
]