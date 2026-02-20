from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . models import Task
# Create your views here.

def task_home(request):
	return render(request, 'tasks/task_home.html', {})

@login_required
def task_list(request):
	tasks = Task.objects.filter(user=request.user).order_by('is_completed')
	return render(request, 'tasks/task_list.html', {'tasks':tasks})

@login_required
def create_task(request):
	if request.method == "POST":
		title = request.POST.get('title')
		description = request.POST.get('description')
		is_completed = True if request.POST.get('is_completed')=='on' else False
		Task.objects.create(
			title = title,
			description = description,
			is_completed = is_completed,
			user = request.user
		)
		return redirect('tasks:task_list')
	return render(request, 'tasks/task_form.html', {})

@login_required
def toggle_task(request, id):
	task = get_object_or_404(Task, id=id, user=request.user)
	task.is_completed = not task.is_completed
	task.save()
	return redirect('tasks:task_list')

@login_required
def edit_task(request, id):
	task = get_object_or_404(Task, id=id, user=request.user)
	if request.method == 'POST':
		title = request.POST.get('title')
		description = request.POST.get('description')
		is_completed = True if request.POST.get('is_completed')=='on' else False
		task.save()
		return redirect('tasks:task_list')
	return render(request, 'tasks/task_form.html', {'task':task})

@login_required
def delete_task(request, id):
	task = get_object_or_404(Task, id=id, user=request.user)
	task.delete()
	return redirect('tasks:task_list')

@login_required
def admin_view(request):
	tasks = Task.objects.all()
	return render(request, 'tasks/admin_view.html', {'tasks':tasks})