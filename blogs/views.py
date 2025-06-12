from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(
        request,
        'blogs/list.html',
        {'posts': posts}
    )
    
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.Status.PUBLISHED)
    return render(
        request,
        'blogs/detail.html',
        {'post':post}
    )