from django.shortcuts import render

from frontend import *
from .models import *

def ind(request):
    posts = Post.objects.all()
    context ={
        "posts": posts
    }
    return render(request, 'index.html', context)