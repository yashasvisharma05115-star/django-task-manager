from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Task

# 1. This is your existing API endpoint (Data Window)
def task_list_api(request):
    tasks = Task.objects.all().values('id', 'title', 'description', 'is_completed', 'created_at')
    return JsonResponse({"status": "success", "data": list(tasks)})

# 2. This is your new Frontend Webpage with a clickable button!
def task_homepage(request):
    if request.method == "POST":
        # When someone clicks the button, grab what they typed and save it
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title:
            Task.objects.create(title=title, description=description)
        return redirect('/') # Reload the page to show the new task
        
    # Get all tasks to display them on the page
    all_tasks = Task.objects.all().order_by('-id')
    return render(request, 'tasks/index.html', {'tasks': all_tasks})