from django.shortcuts import render,redirect
from django.contrib.auth.forms	import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for ' + user)

			return redirect('/login/')
			

	context = {'form':form}
	return render(request, 'signup.html', context)
@csrf_protect
def loginPage(request):
	
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('/mainhome/')
		else:
			
			messages.info(request, 'Username OR password is incorrect')
		context= {'username':username}	

	
	return render(request, 'login.html')

def logoutUser(request):
	logout(request)
	return redirect('/login/')