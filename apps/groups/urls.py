from django.urls import path
from .views import (
    group_list_view,
    group_detail_view,
    group_create_view,
    group_update_view,
    group_delete_view,
)

app_name = 'groups'

urlpatterns = [
    path('', group_list_view, name='group_list'),
    path('<int:group_id>/', group_detail_view, name='group_detail'),
    path('create/', group_create_view, name='group_create'),
    path('<int:group_id>/update/', group_update_view, name='group_update'),
    path('<int:group_id>/delete/', group_delete_view, name='group_delete'),
]
