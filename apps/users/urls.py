from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UserRegisterView, UserProfileView, UserEditView, friend_requests_view, notifications_view

app_name = 'users'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
    path('profile/edit/', UserEditView.as_view(), name='profile_edit'),
    path('friend-requests/', friend_requests_view, name='friend_requests'),
    path('notifications/', notifications_view, name='notifications'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]
