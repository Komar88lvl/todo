from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from tracker.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tracker:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tracker:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tracker:task-list")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tracker:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tracker:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tracker:tag-list")


def toggle_task_complete(request, pk):
    task = Task.objects.get(id=pk)
    task.is_completed = not task.is_completed
    task.save()
    return redirect("tracker:task-list")
