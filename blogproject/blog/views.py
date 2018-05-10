from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Tag
import markdown


def index(request):
    posts = Post.objects.all().order_by('-created_time')
    post_list = []
    for post in posts:
        tags = post.tags. all()
        post_list.append({'post': post, 'tags': tags})
    context = {'posts': posts, 'post_list': post_list}
    return render(request, 'blog/index.html', context)


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    posts = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/detail.html', context={'post': post, 'posts': posts})
