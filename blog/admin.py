from django.contrib import admin
from blog.models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','counted_view', 'status', 'published_date')
    list_filter = ('status',)
    search_fields = ['title', 'content']

admin.site.register(Post,PostAdmin)
