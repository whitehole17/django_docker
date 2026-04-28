from django.urls import path
from . import views

urlpatterns = [
    path('', views.image_upload, name='image_upload'),
    path('success', views.upload_success, name='upload_success'),
]