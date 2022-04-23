from django.urls import path
from .views import (HomePageView, ArticleListView, ArticleDetailView, 
                        ArticleUpdateView, ArticleDeleteView, ArticleCreateView) 

urlpatterns = [
    path('', HomePageView.as_view(), name="blog_home"), 
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('articles/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('articles/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('articles/new/', ArticleCreateView.as_view(), name='article_new'),
    path('articles', ArticleListView.as_view(), name='article_list'),
]
    