from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import logout




class HomePageView(TemplateView):
    template_name = 'home.html'

def logout_view(request):
    logout(request)
    return redirect('users:login')
