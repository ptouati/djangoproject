from django.shortcuts import render
from django.http import HttpResponse

from .models import Posts

# Create your views here.
def index(request):
  #return HttpResponse('HELLO FROM POSTS')

  posts = Posts.objects.all()[:4]

  context = {
    'title': 'Latest Posts test to see if in views',
    'posts': posts
  }

  return render(request, 'posts/index.html', context)

def details(request, id):
  post = Posts.objects.get(id=id)

  context = {
    'post': post
  }

  return render(request, 'posts/details.html', context)