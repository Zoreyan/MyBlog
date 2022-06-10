from urllib import request
from django.shortcuts import render
from .models import *
from django.views import generic
# Create your views here.

def post_list(request):


    search = request.GET.get('search', '')
    if search:
        posts = Post.objects.filter(
            title__icontains = search
        )
    else:
        posts = Post.objects.filter(show=True)



    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)

class PostDetail(generic.DetailView):
    model = Post
    context_object_name = 'post'
    slug_field = 'slug'
    template_name = 'blog/post_detail.html'