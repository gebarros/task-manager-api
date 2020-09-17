from rest_framework import serializers
from .models import TaskList, Tag, Task

class TaskListSerializer(serializers.ModelSerializer):
	class Meta:
		model = TaskList
		fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = '__all__'

class TagShortSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = ('Name',)

class TaskNestedSerializer(serializers.ModelSerializer):
	TaskList = TaskListSerializer(read_only=True)
	Tags = TagShortSerializer(many=True, read_only=True)

	class Meta:
		model = Task
		fields = ('Id', 'Title', 'Notes',
						 'Priority', 'RemindMeOn',
						 'ActivityType', 'Status',
						 'TaskList', 'Tags')

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ('Id', 'Title', 'Notes',
						 'Priority', 'RemindMeOn',
						 'ActivityType', 'Status',
						 'TaskList', 'Tags')
