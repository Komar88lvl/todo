from django.urls import path
from tracker.views import (
    TaskListView,
    TagListView,
    TaskCreateView,
    TagCreateView,
)

urlpatterns = [
    #    path("admin/", admin.site.urls),
    path("", TaskListView.as_view(), name="task-list"),
    path("task_create/", TaskCreateView.as_view(), name="task-create"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tag_create/", TagCreateView.as_view(), name="tag-create"),
]

app_name = "tracker"
