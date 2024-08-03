from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView
from .models import CustomUser, FriendRequest, UserNotification
from .forms import CustomUserCreationForm, CustomUserChangeForm

class UserRegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('users:profile', pk=user.pk)

class UserProfileView(View):
    def get(self, request, pk):
        user = get_object_or_404(CustomUser, pk=pk)
        return render(request, 'users/profile.html', {'user': user})

class UserEditView(UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'profiles/profile_edit.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self):
        return self.request.user

@login_required
def friend_requests_view(request):
    received_requests = FriendRequest.objects.filter(to_user=request.user)
    sent_requests = FriendRequest.objects.filter(from_user=request.user)
    return render(request, 'users/friend_requests.html', {
        'received_requests': received_requests,
        'sent_requests': sent_requests
    })

@login_required
def notifications_view(request):
    notifications = UserNotification.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'users/notifications.html', {'notifications': notifications})
    
