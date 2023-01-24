from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})


def my_learning(request):
    return render(request, 'portfolio/my_learning.html')