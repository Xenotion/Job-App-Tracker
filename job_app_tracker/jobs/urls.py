from django.urls import path 
from . import views

# define the urls
urlpatterns = [
    path('jobs/', views.jobs),
    path('jobs/<int:pk>/', views.job_detail),
]