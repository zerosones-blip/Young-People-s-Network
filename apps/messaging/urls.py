from django.urls import path
from .views import (
    conversation_list_view,
    conversation_detail_view,
    message_create_view,
    message_update_view,
    message_delete_view,
)

app_name = 'messaging'

urlpatterns = [
    path('conversations/', conversation_list_view, name='conversation_list'),
    path('conversation/<int:conversation_id>/', conversation_detail_view, name='conversation_detail'),
    path('conversation/<int:conversation_id>/message/create/', message_create_view, name='message_create'),
    path('message/<int:message_id>/update/', message_update_view, name='message_update'),
    path('message/<int:message_id>/delete/', message_delete_view, name='message_delete'),
]
