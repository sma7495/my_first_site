from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    image= models.ImageField(upload_to='blog/', default= 'blog/default.jpg')
    author= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150)
    content = models.TextField()
    #tag
    category= models.ManyToManyField('Category')
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(default= timezone.now())
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    
class Category (models.Model):
    name=models.CharField(max_length=150)

    def __str__(self):
        return self.name
    

class Comments (models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reply = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=256)
    email = models.EmailField()
    subject = models.CharField(max_length=256)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
