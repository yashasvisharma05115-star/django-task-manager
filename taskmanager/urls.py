from django.contrib import admin
from django.urls import path
from tasks.views import task_list_api, task_homepage # Added task_homepage here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks/', task_list_api),
    path('', task_homepage),  # This blank path '' means your main homepage!
]