from django.urls import path
from .views import (
    post_detail_view,
    post_create_view,
    PostUpdateView,
    PostDeleteView,
    PostListView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)

app_name = 'posts'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', post_detail_view, name='post_detail'),
    path('post/create/', post_create_view, name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/comment/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]
