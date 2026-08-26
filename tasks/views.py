from django.shortcuts import get_object_or_404, redirect, render

from .forms import TaskForm
from .models import Task


def task_list(request):
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('tasks:list')
	else:
		form = TaskForm()

	return render(
		request,
		'tasks/task_list.html',
		{'form': form, 'tasks': Task.objects.all()},
	)


def toggle_task(request, pk):
	if request.method == 'POST':
		task = get_object_or_404(Task, pk=pk)
		task.completed = not task.completed
		task.save(update_fields=('completed',))
	return redirect('tasks:list')
