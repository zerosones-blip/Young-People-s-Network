from django.urls import path
from .views import (
    event_list_view,
    event_detail_view,
    event_create_view,
    event_update_view,
    event_delete_view,
)

app_name = 'events'

urlpatterns = [
    path('', event_list_view, name='event_list'),
    path('<int:event_id>/', event_detail_view, name='event_detail'),
    path('create/', event_create_view, name='event_create'),
    path('<int:event_id>/update/', event_update_view, name='event_update'),
    path('<int:event_id>/delete/', event_delete_view, name='event_delete'),
]
