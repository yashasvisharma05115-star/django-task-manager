from django.contrib import admin
from .models import Task

# This tells the admin panel to show our Tasks table
admin.site.register(Task)