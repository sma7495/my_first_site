from django.urls import path, include
from website import views
urlpatterns = [
    path('', views.index_view ),
    path('about/', views.about_view ),
]
