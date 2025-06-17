from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from taggit.models import Tag

# Create your views here.
def post_list(request, tag_slug=None):
    post_list = Post.objects.filter(status=Post.Status.PUBLISHED)
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])
    paginator = Paginator(post_list, 2)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(
        request,
        'blogs/list.html',
        {'posts': posts, 'tag': tag}
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