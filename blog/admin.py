from django.contrib import admin
from blog.models import Post, Category, Comments
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


class PostAdmin(SummernoteModelAdmin):
    list_display = ('title','counted_view', 'status', 'published_date')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    summernote_fields = ('content',)

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name','post', 'approved', 'created_date')
    list_filter = ('approved',)
    search_fields = ['name', 'post']

admin.site.register(Post,PostAdmin)
admin.site.register(Comments,CommentsAdmin)
admin.site.register(Category)
