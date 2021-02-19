from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .form import *
# Create your views here.
def home (request ):
	return render(request,'home.html')

def mainhome(request):
	return render(request,'home2.html')

def todo(request):
	if not request.user.is_authenticated:
		 return render(request,'login.html')
	
	else:
		task = Task.objects.all()

		form = Taskform()

		if request.method == 'POST':
			form = Taskform(request.POST)
			if form.is_valid():
				form.save()
			return redirect('/')
		context = {'task':task,'form':form}
		return render(request,'base.html',context)

@login_required(login_url='login')
def update(request,pk):
	task= Task.objects.get(id=pk)

	form = Taskform(instance=task)

	if request.method == 'POST':
		form = Taskform(request.POST,instance=task)

		if form.is_valid():
			form.save()
			return redirect('/')


	context = {'form':form}
	return render(request,'update.html',context)

@login_required(login_url='/login/')
def delete(request,pk):

	item = Task.objects.get(id=pk)
	context = {'item':item}
	if request.method == 'POST':
		item.delete()

		return redirect('/')
	return render(request,'delete.html',context)



