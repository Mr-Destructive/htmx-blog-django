from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.createArticle, name='article-create'), 
    path('', views.listArticle, name='article-list'), 
]
