from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(status=Post.Status.PUBLISHED)
    return render(
        request,
        'blogs/list.html',
        {'posts': posts}
    )
    
def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post, 
        slug=post,
        published__year=year,
        published__month=month,
        published__day=day,
        status=Post.Status.PUBLISHED)
    return render(
        request,
        'blogs/detail.html',
        {'post':post}
    )