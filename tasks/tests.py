from django.test import TestCase

from django.urls import reverse

from .models import Task


class TaskModelTests(TestCase):
	def test_task_defaults_to_incomplete(self):
		task = Task.objects.create(title='Read Django docs')

		self.assertFalse(task.completed)
		self.assertEqual(str(task), 'Read Django docs')


class TaskListViewTests(TestCase):
	def test_list_page_shows_tasks(self):
		Task.objects.create(title='Review pull request')

		response = self.client.get(reverse('tasks:list'))

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'tasks/task_list.html')
		self.assertContains(response, 'Review pull request')

	def test_valid_post_creates_task(self):
		response = self.client.post(
			reverse('tasks:list'),
			{'title': 'Write a test'},
		)

		self.assertRedirects(response, reverse('tasks:list'))
		self.assertTrue(Task.objects.filter(title='Write a test').exists())

	def test_blank_post_shows_validation_error(self):
		response = self.client.post(reverse('tasks:list'), {'title': ''})

		self.assertEqual(response.status_code, 200)
		self.assertEqual(Task.objects.count(), 0)
		self.assertContains(response, 'This field is required.')

	def test_toggle_post_changes_completion(self):
		task = Task.objects.create(title='Ship demo')

		response = self.client.post(
			reverse('tasks:toggle', args=[task.pk]),
		)

		task.refresh_from_db()
		self.assertRedirects(response, reverse('tasks:list'))
		self.assertTrue(task.completed)
