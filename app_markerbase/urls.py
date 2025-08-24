from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    ##
    path('add/', views.marker_upload, name='marker_upload'),
    path('edit/<int:pk>/', views.marker_edit, name='marker_edit'),
    path('marker/<int:pk>/', views.marker_detail, name='marker_detail'),
]
