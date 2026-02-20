from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_POST
# Create your views here.

def signup(request):

	if request.method == "POST":

		first_name = request.POST['fname']
		last_name = request.POST['lname']
		email = request.POST['email']
		phone = request.POST['phone']
		pass1 = request.POST['pass1']
		pass2 = request.POST['pass2']

		if pass1 != pass2 :
			return render(request, 'accounts/signup.html', {'error': 'Password do not match!'})
		
		if User.objects.filter(username=email).exists():
			return render(request, 'accounts/signup.html', {'error': 'User Already Exists, use different email'})
		
		user = User.objects.create_user(username=email, email=email, password=pass1)
		user.first_name = first_name
		user.last_name = last_name
		user.save()

		return redirect('accounts:signin')


	return render(request, 'accounts/signup.html', {})

def signin(request):

	if request.method == "POST":

		username = request.POST['email']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user is not None:

			login(request, user)
			return redirect('tasks:task_list')
		
		else:
			return render(request, 'accounts/signin.html', {'error':'incorrect username or password'})

	return render(request, 'accounts/signin.html', {})

@require_POST
def signout(request):
	logout(request)
	return redirect('tasks:task_home')