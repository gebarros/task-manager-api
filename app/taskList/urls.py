from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('taskList', views.TaskListViewSet)
router.register('tags', views.TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
		path('tasks/', views.TaskView.as_view()),
		path('tasks/<uuid:pk>/', views.TaskDetailView.as_view()),
]


