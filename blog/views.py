from django.shortcuts import render, get_object_or_404
from blog import models

def index_view(request):
    posts = models.Post.objects.filter(status = 1).order_by("-published_date")
    contex = {'posts': posts}

    return render( request,'blog/blog-home.html', contex)


def about_view(request, pid):
    post = get_object_or_404(models.Post, pk=pid, status=1)
    contex = {"post": post}
    return render( request,'blog/blog-single.html', contex)