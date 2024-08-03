from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView
from .models import Profile, Connection, ProfileView
from .forms import ProfileForm, SkillForm, ExperienceForm, EducationForm, SocialLinkForm

@login_required
def profile_detail_view(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    return render(request, 'profiles/profile_detail.html', {'profile': profile})

@login_required
def profile_edit_view(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile:profile_detail', pk=profile.pk)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profiles/profile_edit.html', {'form': form})

@login_required
def connection_requests_view(request):
    received_requests = Connection.objects.filter(to_profile=request.user.profile, accepted=False)
    sent_requests = Connection.objects.filter(from_profile=request.user.profile, accepted=False)
    return render(request, 'profiles/connection_requests.html', {
        'received_requests': received_requests,
        'sent_requests': sent_requests
    })

@login_required
def profile_views_view(request):
    profile_views = ProfileView.objects.filter(profile=request.user.profile).order_by('-timestamp')
    return render(request, 'profiles/profile_views.html', {'profile_views': profile_views})

class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profiles/profile_edit.html'
    success_url = reverse_lazy('profiles:profile_detail')

    def get_object(self):
        return self.request.user.profile
