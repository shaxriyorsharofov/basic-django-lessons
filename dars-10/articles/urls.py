from django.urls import path

from .views import ArticleListView, ArticleUpdateView, ArticleDeleteView, ArticleDetailView, ArticleCreateView


urlpatterns = [
    path('article_list/<int:pk>/edit/', ArticleUpdateView.as_view(), name="article_edit"),
    path('article_list/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('article_list/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('article_list/', ArticleListView.as_view(), name='article_list'),
]

