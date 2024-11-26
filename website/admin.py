from django.contrib import admin
from website import models
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')
    list_filter = ('name', 'created_date')

admin.site.register(models.Contact,ContactAdmin)