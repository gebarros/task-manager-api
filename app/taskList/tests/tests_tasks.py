import json, logging
from rest_framework import status
from django.test import TestCase, Client
from taskList.models import TaskList, Task, Tag
from taskList.serializer import TaskNestedSerializer, TaskSerializer

logging.disable(logging.WARNING)

# initialize the APIClient app
client = Client()
class TaskViewTest(TestCase):
	""" Test module for Tag """
	def setUp(self):
		tasklist = TaskList.objects.create(Id= "c60b4c69-b26a-4f66-aa59-dfdb925a75f8", Name= "Trabalho",)
		my_task = Task.objects.create(Id="107defa7-14f0-4b20-9a75-4c437be9c375", Title="Fazer teste",
												Notes=None, Priority=0, RemindMeOn= "2020-09-08", ActivityType= "indoors",
												Status= "open", TaskList= tasklist,)
		my_task.Tags.create(Id= "72b283e7-1a42-456e-be00-ab5437afb400", Name= "Urgente", Count=0)


		self.valid_task = {
			"Title": "Corrida",
			"Notes": None,
			"Priority": 0,
			"RemindMeOn": "2020-09-08",
			"ActivityType": "indoors",
			"Status": "open",
			"TaskList": "c60b4c69-b26a-4f66-aa59-dfdb925a75f8",
			"Tags": [
            "72b283e7-1a42-456e-be00-ab5437afb400"
        ]
		}

		self.invalid_task = {
			"Title": "",
			"Notes": None,
			"Priority": 0,
			"RemindMeOn": "2020-09-08",
			"ActivityType": "indoors",
			"Status": "open",
			"TaskList": "c60b4c69-b26a-4f66-aa59-dfdb925a75f8",
			"Tags": [
            "72b283e7-1a42-456e-be00-ab5437afb400"
        ]
		}

	def test_get_all_tasks(self):
		response = client.get('/tasks/')
		tasks = Task.objects.all()
		serializer = TaskNestedSerializer(tasks, many=True)
		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_create_valid_task(self):
		response = client.post('/tasks/', data=json.dumps(self.valid_task),
														content_type='application/json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_create_invalid_task(self):
		response = client.post('/tasks/', data=json.dumps(self.invalid_task),
														content_type='application/json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class TaskDetailViewTest(TestCase):
	""" Test module for Task """
	def setUp(self):
		tasklist = TaskList.objects.create(Id= "c60b4c69-b26a-4f66-aa59-dfdb925a75f8", Name= "Trabalho",)
		my_task = Task.objects.create(Id="107defa7-14f0-4b20-9a75-4c437be9c375", Title="Fazer teste",
												Notes=None, Priority=0, RemindMeOn= "2020-09-08", ActivityType= "indoors",
												Status= "open", TaskList= tasklist,)
		my_task.Tags.create(Id= "72b283e7-1a42-456e-be00-ab5437afb400", Name= "Urgente", Count=0)

		self.valid_update_task = {
			"Title": "Fazer Testes",
			"Notes": "My notes",
			"Priority": 0,
			"RemindMeOn": "2020-09-08",
			"ActivityType": "indoors",
			"Status": "done",
			"TaskList": "c60b4c69-b26a-4f66-aa59-dfdb925a75f8",
			"Tags": [
            "72b283e7-1a42-456e-be00-ab5437afb400"
        ]
		}

		self.invalid_update_task = {
			"Title": "",
			"Notes": "My notes",
			"Priority": 0,
			"RemindMeOn": "2020-09-08",
			"ActivityType": "indoors",
			"Status": "done",
			"TaskList": "c60b4c69-b26a-4f66-aa59-dfdb925a75f8",
			"Tags": [
            "72b283e7-1a42-456e-be00-ab5437afb400"
        ]
		}
		self.valid_partial_update_task = {
			"Notes": "My partial notes",
			"Status": "done",
		}

		self.invalid_partial_update_task = {
			"Notes": "My partial notes",
			"Status": "",
		}

	def test_get_object_error_id(self):
			task = Task.objects.get(Id="107defa7-14f0-4b20-9a75-4c437be9c375")
			self.assertNotEqual(task.Id, "107defa7-14f0-4b20-9a75-4c437be9c445")

	def test_get_object(self):
		task = Task.objects.get(Id="107defa7-14f0-4b20-9a75-4c437be9c375")
		self.assertTrue(isinstance(task, Task))

	def test_get_task(self):
		response = client.get('/tasks/107defa7-14f0-4b20-9a75-4c437be9c375/')
		task= Task.objects.get(Id="107defa7-14f0-4b20-9a75-4c437be9c375")
		serializer = TaskNestedSerializer(task)
		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_invalid_task(self):
		response = client.get('/tasks/72b283e7-1a42-456e-be00-ab5437af/')
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

	def test_update_valid_task(self):
		response = client.put('/tasks/107defa7-14f0-4b20-9a75-4c437be9c375/', data=json.dumps(self.valid_update_task),
														content_type='application/json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_update_invalid_task(self):
		response = client.put('/tasks/107defa7-14f0-4b20-9a75-4c437be9c375/', data=json.dumps(self.invalid_update_task),
														content_type='application/json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_partial_update_valid_task(self):
		response = client.patch('/tasks/107defa7-14f0-4b20-9a75-4c437be9c375/', data=json.dumps(self.valid_partial_update_task),
														content_type='application/json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_partial_update_invalid_task(self):
		response = client.patch('/tasks/107defa7-14f0-4b20-9a75-4c437be9c375/', data=json.dumps(self.invalid_partial_update_task),
														content_type='application/json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_valid_delete_task(self):
		response = client.delete('/tasks/107defa7-14f0-4b20-9a75-4c437be9c375/')
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

	def test_invalid_delete_task(self):
		response = client.delete('/tasks/bd0bd626-eca7-43d3-b5ab-/')
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
