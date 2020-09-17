import json, logging
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from taskList.models import TaskList
from taskList.serializer import TaskListSerializer

logging.disable(logging.WARNING)

# initialize the APIClient app
client = Client()
class TaskListTest(TestCase):
	""" Test module for TaskList """
	def setUp(self):
		TaskList.objects.create(Id= "2718e8be-61c8-465e-ac65-cfe7416f24f7", Name= "Familia")
		TaskList.objects.create(Id= "c60b4c69-b26a-4f66-aa59-dfdb925a75f8", Name= "Trabalho")

		self.valid_taskList = {
			'Name': 'Voluntariado'
		}
		self.invalid_taskList = {
			'Name': ''
		}
		self.valid_update_taskList = {
			'Name': 'Family'
		}
		self.invalid_update_taskList = {
			'Name': ''
		}

	def test_get_all_taskList(self):
		response = client.get('/taskList/')
		task_list = TaskList.objects.all()
		serializer = TaskListSerializer(task_list, many=True)
		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_taskList(self):
		response = client.get('/taskList/2718e8be-61c8-465e-ac65-cfe7416f24f7/')
		task = TaskList.objects.get(Id="2718e8be-61c8-465e-ac65-cfe7416f24f7")
		serializer = TaskListSerializer(task)
		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_invalid_taskList(self):
		response = client.get('/taskList/2718e8be-61c8-465e-ac65-cfe7416f/')
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

	def test_create_valid_taskList(self):
		response = client.post('/taskList/', data=json.dumps(self.valid_taskList),
														content_type='application/json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_create_invalid_taskList(self):
		response = client.post('/taskList/', data=json.dumps(self.invalid_taskList),
														content_type='application/json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_update_valid_taskList(self):
		response = client.put('/taskList/2718e8be-61c8-465e-ac65-cfe7416f24f7/', data=json.dumps(self.valid_update_taskList),
														content_type='application/json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_update_invalid_taskList(self):
		response = client.put('/taskList/2718e8be-61c8-465e-ac65-cfe7416f24f7/', data=json.dumps(self.invalid_update_taskList),
														content_type='application/json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_valid_delete_taskList(self):
		response = client.delete('/taskList/c60b4c69-b26a-4f66-aa59-dfdb925a75f8/')
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

	def test_invalid_delete_taskList(self):
		response = client.delete('/taskList/c60b4c69-b26a-4f66-aa59-dfdb925a7/')
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
