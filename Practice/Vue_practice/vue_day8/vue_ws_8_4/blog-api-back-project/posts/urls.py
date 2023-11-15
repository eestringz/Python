from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_list),
    path('category/', views.category_list),
    path('post/', views.post_list),
    path('posts/<int:post_pk>/', views.post_detail),
    path('posts/<int:post_pk>/comments/', views.comment_create),
    path('posts/<int:post_pk>/comments/<int:comment_pk>/', views.comment_delete),
]
