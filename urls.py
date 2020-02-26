from django.urls import path

from .views import post_list, post_details, posts_update, posts_create, post_delete

app_name ='project5'

urlpatterns=[
    path('', post_list, name='project5'),
    path('post_details/<slug:slug>/', post_details, name='post_details'),
    path('posts_update/<slug:slug>/', posts_update, name='posts_update'),
    path('posts_create/', posts_create, name='posts_create'),
    path('post_delete/<slug:slug>', post_delete, name='post_delete')

]