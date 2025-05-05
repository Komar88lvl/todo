from django.urls import path
from tracker.views import TaskListView, TagListView

urlpatterns = [
    #    path("admin/", admin.site.urls),
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
]
