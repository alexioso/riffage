from django.http import *
from django.shortcuts import render, get_object_or_404, redirect
from .forms import MessageForm
from .models import Message
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt

def inbox(request):
	username = request.user.username
	messages = Message.objects.filter(message_received_by=username)
	params = {}
	params['category'] = 'inbox'
	return render(request, 'inbox.html',
		{'params': params,
		 'messages': messages,
		 })


@csrf_exempt
def message_send(request):
	params = {}
	params['category'] = 'inbox'

	if request.method == 'POST':
		send_to_user = request.POST.get('send_to_user')
		subject = request.POST.get('subject')
		message = request.POST.get('message')
		if send_to_user and subject and message:
			msg = Message(message_sent_by=request.user.username, 
						  message_received_by=send_to_user,
						  subject=subject,
						  body=message)
			msg.save()
			params['message_saved'] = True
		else: 
			params['message_saved'] = False
		return JsonResponse(params)

	users = User.objects.all()
	users = User.objects.exclude(username=request.user.username)
	return render(request, 'message_send.html', {'params': params, 'users':users})

def message_detail(request, pk):
	params = {}
	params['category'] = 'inbox'
	
	message = get_object_or_404(Message, pk=pk)
	message.read = True
	message.save()
	return render(request, 'message_detail.html', {'params': params, 'message': message})

def message_delete(request, pk):
	message = get_object_or_404(Message, pk=pk)
	message.delete()
	return redirect('inbox')
	
