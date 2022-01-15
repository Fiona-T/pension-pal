"""URL paths for the 'pensions' app (add, view, edit, delete pension)"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyPensions.as_view(), name='my_pensions'),
    path('add/', views.AddPension.as_view(), name='add_pension'),
    path(
        'success/<pension_id>',
        views.AddPensionSuccess.as_view(),
        name='add_pension_success'
        ),
    path(
        'edit/<pension_id>',
        views.EditPension.as_view(),
        name='edit_pension'
        ),
    path(
        'delete/<pension_id>',
        views.DeletePension.as_view(),
        name='delete_pension'
        ),
    path(
        'view-details/<pension_id>',
        views.PensionDetails.as_view(),
        name='view_pension'),
]
