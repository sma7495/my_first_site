from django.shortcuts import render, get_object_or_404, redirect
from blog import models
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def index_view(request):
    posts = models.Post.objects.filter(status = 1).order_by("-published_date")
    p = Paginator(posts,3)
    try:
        posts = p.page(request.GET.get("page"))
    except PageNotAnInteger:
        posts = p.page(1)
    except EmptyPage:
        posts = p.page(1)
        


    contex = {'posts': posts}

    return render( request,'blog/blog-home.html', contex)


def about_view(request, pid):
    post = get_object_or_404(models.Post, pk=pid, status=1)
    contex = {"post": post}
    return render( request,'blog/blog-single.html', contex)


def category_view(request, cat=None, writer=None):
    posts = None
    if cat:
        posts = models.Post.objects.filter(status = 1, category__name = cat).order_by("-published_date")

    if writer:
        posts = models.Post.objects.filter(status = 1, author__first_name = writer).order_by("-published_date")

    p = Paginator(posts,3)
    try:
        posts = p.page(request.GET.get("page"))
    except PageNotAnInteger:
        posts = p.page(1)
    except EmptyPage:
        posts = p.page(1)

    contex = {'posts': posts}
    return render( request,'blog/blog-home.html', contex)   

def search_view(request):
    if request.method == "GET":
        if s:=request.GET.get("s"):
            posts = models.Post.objects.filter(status = 1).filter(Q(title__icontains = s) | Q(content__icontains = s))
            p = Paginator(posts,3)
            try:
                posts = p.page(request.GET.get("page"))
            except PageNotAnInteger:
                posts = p.page(1)
            except EmptyPage:
                posts = p.page(1)
                
            contex = {'posts': posts, 'search':s}
            return render( request,'blog/blog-home.html', contex)
        else:
            return redirect("website:index")
