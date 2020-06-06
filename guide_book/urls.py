from django.urls import path

from . import views

urlpatterns = [
    path('task', views.NextTaskView.as_view(), name='next-task'),
]
