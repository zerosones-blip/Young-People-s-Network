from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Conversation, Message
from .forms import MessageForm

@login_required
def conversation_list_view(request):
    conversations = request.user.conversations.all()
    return render(request, 'messaging/conversation_list.html', {'conversations': conversations})

@login_required
def conversation_detail_view(request, conversation_id):
    conversation = get_object_or_404(Conversation, pk=conversation_id)
    messages = conversation.messages.all()
    return render(request, 'messaging/conversation_detail.html', {'conversation': conversation, 'messages': messages})

@login_required
def message_create_view(request, conversation_id):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            conversation = get_object_or_404(Conversation, pk=conversation_id)
            message = form.save(commit=False)
            message.conversation = conversation
            message.sender = request.user
            message.save()
            return redirect('messaging:conversation_detail', conversation_id=conversation_id)
    else:
        form = MessageForm()
    return render(request, 'messaging/message_create.html', {'form': form})

@login_required
def message_update_view(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    if request.method == 'POST':
        form = MessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            return redirect('messaging:conversation_detail', conversation_id=message.conversation.pk)
    else:
        form = MessageForm(instance=message)
    return render(request, 'messaging/message_update.html', {'form': form})

@login_required
def message_delete_view(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    if request.method == 'POST':
        message.delete()
        return redirect('messaging:conversation_detail', conversation_id=message.conversation.pk)
    return render(request, 'messaging/message_delete.html', {'message': message})
