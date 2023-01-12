from django.shortcuts import render, redirect
from .models import TaskList
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "New Task Added!")
        return redirect('todolist')
    else:
        all_tasks = TaskList.objects.filter(owner=request.user)
        paginator = Paginator(all_tasks, 10)
        page = request.GET.get('page')
        all_tasks = paginator.get_page(page)
    return render(request, "task.html", context={'all_tasks': all_tasks})


@login_required
def delete(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.owner == request.user:
        task.delete()
        messages.success(request, "Selected Task Deleted!")
    else:
        messages.success(request, "Access Restricted, You are not Allowed!")

    return redirect('todolist')


@login_required
def edit(request, task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
        messages.success(request, "Edited Task")
        return redirect('todolist')
    else:
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request, "edit.html", context={'all_tasks': task_obj})


@login_required
def complete(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.owner == request.user:
        task.done = True
        task.save()
    else:
        messages.success(request, "Access Restricted, You are not Allowed!")
    return redirect('todolist')


@login_required
def pending(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()

    return redirect('todolist')


def index(request):
    context = {
        "welcome_text": "Welcome To Index Page",
    }
    return render(request, "index.html", context)


def contact(request):
    context = {
        "welcome_text": "Welcome To Contact Me",
    }
    return render(request, "contact.html", context)


def about(request):
    context = {
        "about_text": "Welcome To About Me",
    }
    return render(request, "about.html", context)
