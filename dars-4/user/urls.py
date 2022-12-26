from django.urls import path
from .views import HomeView, HomeDetailView, BlogCreateView, BlogUpdate

urlpatterns = [
    path("post/<int:pk>/edit", BlogUpdate.as_view(), name='post_edit'),
    path("post/new/", BlogCreateView.as_view(), name='create_view'),
    path("", HomeView.as_view(), name='home'),
    path("post/<int:pk>/", HomeDetailView.as_view(), name='home_detail'),
]