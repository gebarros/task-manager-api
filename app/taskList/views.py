import logging
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ValidationError

from .models import TaskList, Tag, Task
from .serializer import TaskListSerializer, TagSerializer, TaskSerializer, TaskNestedSerializer

logger = logging.getLogger('django')
class TaskListViewSet(viewsets.ModelViewSet):
	'''
	All HTTP methods allowed for TaskList:
		http://127.0.0.1:8000/taskList/
		http://127.0.0.1:8000/taskList/uuid/
	'''
	queryset = TaskList.objects.all()
	serializer_class = TaskListSerializer

class TagViewSet(viewsets.ModelViewSet):
	'''
	All HTTP methods allowed for TaskList:
		http://127.0.0.1:8000/tags/
		http://127.0.0.1:8000/tags/uuid/
	'''
	queryset = Tag.objects.all()
	serializer_class = TagSerializer

class TaskView(APIView):
	"""
		List all Tasks, or create a new task: http://127.0.0.1:8000/tasks/
	"""

	def get(self, request, format=None):
		tasks = Task.objects.all()
		serializer = TaskNestedSerializer(tasks, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = TaskSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()

			# update number times a tag is been used
			tags_used = serializer.data['Tags']
			for tag in tags_used:
				tasks = Task.objects.filter(Tags__Id=tag)
				total = tasks.count()
				tag_model = Tag.objects.get(Id=tag)
				tag_model.Count = total
				tag_model.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetailView(APIView):
	"""
		Retrieve, update or delete a Task: http://127.0.0.1:8000/tasks/uuid/
	"""

	def get(self, request, pk, format=None):
		task = Task.objects.get(Id=pk)
		serializer = TaskNestedSerializer(task)
		return Response(serializer.data)


	def put(self, request, pk, format=None):
		task = Task.objects.get(Id=pk)
		serializer = TaskSerializer(task, data=request.data)
		if serializer.is_valid():
				serializer.save()

				# update number times a tag is been used
				tags_used = serializer.data['Tags']
				for tag in tags_used:
					tasks = Task.objects.filter(Tags__Id=tag)
					total = tasks.count()
					tag_model = Tag.objects.get(Id=tag)
					tag_model.Count = total
					tag_model.save()
					return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def patch(self, request, pk, format=None):
		task = Task.objects.get(Id=pk)
		serializer = TaskSerializer(task, data=request.data, partial=True)
		if serializer.is_valid():
				serializer.save()

				# update number times a tag is been used
				tags_used = serializer.data['Tags']
				for tag in tags_used:
					tasks = Task.objects.filter(Tags__Id=tag)
					total = tasks.count()
					tag_model = Tag.objects.get(Id=tag)
					tag_model.Count = total
					tag_model.save()
					return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		task = Task.objects.get(Id=pk)
		task.delete()
		return Response({'Object deleted!'},status=status.HTTP_204_NO_CONTENT)
