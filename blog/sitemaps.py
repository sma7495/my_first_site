from django.contrib import sitemaps
from django.urls import reverse
from blog.models import Post

class BlogSitemap(sitemaps.Sitemap):
    prioriy: 0.8
    changefreq = 'weeekly'

    def items(self):
        return Post.objects.filter(status = True)
    
    def location(self, item):
        return reverse('blog:single-blog', kwargs={'pid': item.id})
    
    
    