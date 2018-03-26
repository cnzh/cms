from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.filter(published_date__isnull=False).order_by('-published_date')
    return render(request, 'index.html', {'posts': posts})
