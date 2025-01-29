from django import template
from blog import models

register = template.Library()

@register.simple_tag(name="posts")
def fun():
    posts = models.Post.objects.filter(status = 1).order_by("-counted_view")[0:3]

    return posts

@register.simple_tag(name="reply")
def fun(pid,cid=0):
    if cid:
        replies = models.Comments.objects.filter(post__id = pid, reply__id = cid, approved = True)
    else:
        replies = None
    return replies

@register.inclusion_tag("blog/blog-category.html")
def blog_category():
    categories = models.Category.objects.all()
    return {'categories':categories}

@register.filter()
def blog_cat_post_count(cat):
    return cat.post_set.filter(status = 1).count()
