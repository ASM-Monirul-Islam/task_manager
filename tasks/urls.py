from django.urls import path
from . import views
app_name='tasks'
urlpatterns = [
	path('', views.task_home, name='task_home'),
	path('task_list/', views.task_list, name='task_list'),
	path('create_task/', views.create_task, name='create_task'),
	path('toggle_task/<int:id>', views.toggle_task, name='toggle_task'),
	path('edit_task/<int:id>', views.edit_task, name='edit_task'),
	path('delete_task/<int:id>', views.delete_task, name='delete_task'),
]
