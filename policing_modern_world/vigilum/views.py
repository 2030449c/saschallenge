from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
import json
from vigilum.models import ut, Userc
from django.contrib.auth.models import User, Permission
from django.contrib.auth import models
from django.utils.timezone import now as utcnow
import datetime

def index(request):
	if request.method == 'POST':
		print request.POST
	if request.user.username and request.user.profile.is_user:
		return render(request, 'index.html')
	else:
		return HttpResponseRedirect(reverse('login'))


def login(request):
	if request.user.username and request.user.profile.is_user:
		return HttpResponseRedirect(reverse('index'))
	context = {'error':''}

	if request.method == 'POST':
		username = request.POST.get('username','') #return '' if no username
		password = request.POST.get('password','')

		user = auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request,user)
			cu = request.user.profile
			cu.is_user = True
			cu.last_accessed = utcnow()
			cu.save()



			return HttpResponseRedirect(reverse('index'))
		else:
			context['error'] = 'Wrong username and/or password. Try again.'
			return render(request,'login.html',context)


	context.update(csrf(request))
	return render(request,'login.html',context)

def logout(request):
	cu = request.user.profile
	cu.is_chat_user = False
	cu.save()
	return render(request,'logout.html')

