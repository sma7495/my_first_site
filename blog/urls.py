from django.urls import path, include
from blog import views


app_name = 'blog'
urlpatterns = [
    path('', views.index_view , name= 'index-blog'),
    path('<int:pid>/', views.about_view, name= 'single-blog' ),
    path('category/<str:cat>/', views.category_view, name= 'category-blog' ),
    path('writer/<str:writer>/', views.category_view, name= 'writer-blog' ),
    path('search/', views.search_view, name= 'search-blog' ),
]
