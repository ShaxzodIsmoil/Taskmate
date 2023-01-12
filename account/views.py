from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import CustomUserCreationForm


# Create your views here.
def register_user(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New User created!")
            return redirect('todolist')
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form
    }
    return render(request, "accounts/index.html", context)


