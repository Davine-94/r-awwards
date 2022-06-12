from django.urls import path
from rest_framework import routers
from .views import PostListView, PostDetailView, PostCreateView
from . import views

urlpatterns = [
  path('', PostListView.as_view(), name='homepage'), 
  path('inspiration/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
  path('post/new', PostCreateView.as_view(), name='new_post'),
  path('search-results/', views.search, name='post-search'),
  path('api/v1/projects', views.ProjectList.as_view()),
  path('inspiration/rate/<int:pk>/', views.rate_project, name='rate-project'),
  # path('api/v1/projects/<int:pk>/ratings/', views.RatingsList.as_view(), name='rate_post'),
]