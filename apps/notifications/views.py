from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Notification

@login_required
def notification_list_view(request):
    notifications = request.user.notifications.all()
    return render(request, 'notifications/notification_list.html', {'notifications': notifications})
