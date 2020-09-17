import json, logging
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from taskList.models import Tag
from taskList.serializer import TagSerializer

logging.disable(logging.WARNING)

# initialize the APIClient app
client = Client()

class TagTest(TestCase):
	""" Test module for Tag """
	def setUp(self):
		Tag.objects.create(Id= "72b283e7-1a42-456e-be00-ab5437afb400", Name= "Urgente", Count=0)
		Tag.objects.create(Id= "bd0bd626-eca7-43d3-b5ab-02d4119c63a4", Name= "Normal", Count=0)

		self.valid_tag = {
			'Name': 'Final de semana',
			'Count': 0
		}
		self.invalid_tag = {
			'Name': '',
			'Count': 0
		}
		self.valid_update_tag = {
			'Name': 'Weekend',
			'Count': 0
		}
		self.invalid_update_tag = {
			'Name': '',
			'Count': 0
		}

	def test_get_all_tags(self):
		response = client.get('/tags/')
		tags = Tag.objects.all()
		serializer = TagSerializer(tags, many=True)
		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_tag(self):
		response = client.get('/tags/72b283e7-1a42-456e-be00-ab5437afb400/')
		tag= Tag.objects.get(Id="72b283e7-1a42-456e-be00-ab5437afb400")
		serializer = TagSerializer(tag)
		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_invalid_tag(self):
		response = client.get('/tags/72b283e7-1a42-456e-be00-ab5437af/')
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

	def test_create_valid_tag(self):
		response = client.post('/tags/', data=json.dumps(self.valid_tag),
														content_type='application/json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_create_invalid_tag(self):
		response = client.post('/tags/', data=json.dumps(self.invalid_tag),
														content_type='application/json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_update_valid_tag(self):
		response = client.put('/tags/bd0bd626-eca7-43d3-b5ab-02d4119c63a4/', data=json.dumps(self.valid_update_tag),
														content_type='application/json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_update_invalid_tag(self):
		response = client.put('/tags/bd0bd626-eca7-43d3-b5ab-02d4119c63a4/', data=json.dumps(self.invalid_update_tag),
														content_type='application/json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_valid_delete_tag(self):
		response = client.delete('/tags/bd0bd626-eca7-43d3-b5ab-02d4119c63a4/')
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

	def test_invalid_delete_tag(self):
		response = client.delete('/tags/bd0bd626-eca7-43d3-b5ab-02d4119/')
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
