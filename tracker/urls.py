from django.urls import path
from tracker.views import (
    TaskListView,
    TagListView,
    TaskCreateView,
    TagCreateView,
    TaskUpdateView,
    TagUpdateView,
)

urlpatterns = [
    #    path("admin/", admin.site.urls),
    path("", TaskListView.as_view(), name="task-list"),
    path("task_create/", TaskCreateView.as_view(), name="task-create"),
    path("task_update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),

    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tag_create/", TagCreateView.as_view(), name="tag-create"),
    path("tag_update/<int:pk>/", TagUpdateView.as_view(), name="tag-update"),
]

app_name = "tracker"
