from django.urls import path
from .views import hello_view, post_list, create_post, delete_post

urlpatterns = [
    path('', hello_view),
    path('post_list', post_list, name='post_list'),
    path('create_post', create_post, name='create_post'),
    path('delete_post/<int:post_id>', delete_post, name='delete_post'),
]