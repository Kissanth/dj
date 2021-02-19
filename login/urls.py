from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
	
	path('login/',views.loginPage,name='loginsys'),
	path('signup/',views.registerPage,name='signup'),
	path('logout/',views.logoutUser,name='logout')
	


]