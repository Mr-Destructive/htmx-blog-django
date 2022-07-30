from django.urls import path
from . import views

urlpatterns = [
    path('', views.listArticle, name='article-list'), 
    path('<int:pk>', views.detailArticle, name='article-detail'), 
    path('create/', views.createArticle, name='article-create'), 
    path('delete/<int:pk>', views.deleteArticle, name='article-delete'), 
]
