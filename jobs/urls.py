from django.urls import path

from jobs import views

urlpatterns = [
    path('joblist/', views.joblist, name='joblist'),
    path('job/<int:job_id>/', views.detail, name='detail'),
]