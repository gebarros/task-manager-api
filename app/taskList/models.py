from django.db import models
from simple_history.models import HistoricalRecords
import uuid

ACTIVITY_TYPE = (
		("indoors", "indoors"),
		("outdoors", "outdoors"),
)

STATUS = (
		("open", "open"),
		("done", "done"),
)

class TaskList(models.Model):
	"""Model definition for TaskList."""
	Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	Name = models.CharField("Nome da Tarefa", max_length=255)
	History = HistoricalRecords()

class Tag(models.Model):
	"""Model definition for Tag."""
	Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	Name = models.CharField("Nome da Etiqueta", max_length=255)
	Count = models.IntegerField("No. de utilizações", default=0)
	History = HistoricalRecords()

class Task(models.Model):
	"""Model definition for Task."""
	Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	Title = models.CharField("Título", max_length=255)
	Notes = models.TextField("Notas", null=True, blank=True)
	Priority = models.IntegerField("Prioridade")
	RemindMeOn = models.DateField("Lembrar em", auto_now=False, auto_now_add=False)
	ActivityType = models.CharField("Tipo de Atividade", max_length=50, choices=ACTIVITY_TYPE)
	Status = models.CharField("Status", max_length=50, choices=STATUS)
	TaskList = models.ForeignKey(TaskList, on_delete=models.CASCADE)
	Tags = models.ManyToManyField(Tag)
	History = HistoricalRecords()


