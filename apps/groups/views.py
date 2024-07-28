from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Group
from .forms import GroupForm

@login_required
def group_list_view(request):
    groups = Group.objects.all()
    return render(request, 'groups/group_list.html', {'groups': groups})

@login_required
def group_detail_view(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    return render(request, 'groups/group_detail.html', {'group': group})

@login_required
def group_create_view(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save()
            group.members.add(request.user)
            return redirect('groups:group_detail', group_id=group.pk)
    else:
        form = GroupForm()
    return render(request, 'groups/group_create.html', {'form': form})

@login_required
def group_update_view(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('groups:group_detail', group_id=group.pk)
    else:
        form = GroupForm(instance=group)
    return render(request, 'groups/group_update.html', {'form': form})

@login_required
def group_delete_view(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    if request.method == 'POST':
        group.delete()
        return redirect('groups:group_list')
    return render(request, 'groups/group_delete.html', {'group': group})
