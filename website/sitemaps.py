from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSiremap(sitemaps.Sitemap):
    prioriy: 0.5
    changefreq = 'daily'

    def items(self):
        return ['website:index', 'website:about', 'website:contact']
    
    def location(self, item):
        return reverse(item)
    