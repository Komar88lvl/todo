from django.shortcuts import render
from django.views import generic

from tracker.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"


class TagListView(generic.ListView):
    model = Tag