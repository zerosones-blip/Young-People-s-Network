from django.urls import path
from .views import profile_detail_view, profile_edit_view, connection_requests_view, profile_views_view

app_name = 'profiles'

urlpatterns = [
    path('<int:pk>/', profile_detail_view, name='profile_detail'),
    path('edit/', profile_edit_view, name='profile_edit'),
    path('connection-requests/', connection_requests_view, name='connection_requests'),
    path('profile-views/', profile_views_view, name='profile_views'),
]
