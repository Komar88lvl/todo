from django.urls import path
from tracker.views import (
    TaskListView,
    TagListView,
    TaskCreateView,
)

urlpatterns = [
    #    path("admin/", admin.site.urls),
    path("", TaskListView.as_view(), name="task-list"),
    path("taskcreate/", TaskCreateView.as_view(), name="task-create"),
    path("tags/", TagListView.as_view(), name="tag-list"),
]

app_name = "tracker"
