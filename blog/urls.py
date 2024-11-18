from django.urls import path, include
from blog import views


app_name = 'blog'
urlpatterns = [
    path('', views.index_view , name= 'index-blog'),
    path('single/', views.about_view, name= 'single-blog' ),
]
