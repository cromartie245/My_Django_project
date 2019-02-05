from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Post

posts = [
    {
        'author': 'Haynes Cromartie',
        'title': 'Blog post 1',
        'date_added': 'January 7, 2019',
        'content': 'My first Post',

    },

    {
        'author': 'Renee Cromartie',
        'title': 'Blog post 2',
        'date_added': 'January 8, 2019',
        'content': 'My second Post',
    }

]


def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
