"""URL paths for the 'jobs' app (add, view, edit, delete jobs)"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyJobs.as_view(), name='my_jobs'),
    path('add/', views.AddJob.as_view(), name='add_job'),
    path('success/', views.AddJobSuccess.as_view(), name='add_job_success'),
    path('edit/<job_id>', views.EditJob.as_view(), name='edit_job'),
    path('delete/<job_id>', views.DeleteJob.as_view(), name='delete_job')
]
