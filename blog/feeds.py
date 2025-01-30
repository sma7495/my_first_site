from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post


class LatestEntriesFeed(Feed):
    title = "Latest Posts"
    link = "rss/feed/"
    description = "latest Post"

    def items(self):
        return Post.objects.filter(status = True).order_by('published_date')
    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse("blog:single-blog", args=[item.pk])