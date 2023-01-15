from django.shortcuts import render

from .models import Post


def index(request):
    return render(request, 'posts/index.html')
