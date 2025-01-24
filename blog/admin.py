from django.contrib import admin
from blog.models import Post, Category
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


class PostAdmin(SummernoteModelAdmin):
    list_display = ('title','counted_view', 'status', 'published_date')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    summernote_fields = ('content',)


admin.site.register(Post,PostAdmin)

admin.site.register(Category)
