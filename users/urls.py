from django.urls import path
from . import views
from .views import ProfileList
 
urlpatterns = [
  path('profile/', views.profile, name='profile'),
  path('git', views.ProfileList.as_view()),
]