from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
import json
from vigilum.models import ut, PoliceOfficer, Crime
from django.contrib.auth.models import User, Permission
from django.contrib.auth import models
from django.utils.timezone import now as utcnow
from django.core import serializers

def index(request):
        context={"error":"Please fill in all forms."}
	if request.method == 'POST':
		xy = request.POST.get('xy','')
		addr = request.POST.get('addr','')
		ct = request.POST.get('ct','')
		cname = request.POST.get('cname','')
		if xy != "" and addr !="" and ct != "" and cname !="":
                        m = Crime(coordinates=str(xy),address=str(addr),types=str(ct),callerName=str(cname))
                        m.save()
                else:
                        return render(request, 'index.html', context)
	if request.user.username and request.user.profile.is_operator:
		json_serializer = serializers.get_serializer("json")()
		crimes = json_serializer.serialize(Crime.objects.all(), ensure_ascii=False)
		print crimes
		return render(request, 'index.html', {'crimes':crimes})
	else:
		return HttpResponseRedirect(reverse('login'))


def login(request):
	if request.user.username and request.user.profile.is_operator:
		return HttpResponseRedirect(reverse('index'))
	context = {'error':''}

	if request.method == 'POST':
		username = request.POST.get('username','') #return '' if no username
		password = request.POST.get('password','')

		user = auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request,user)
			cu = request.user.profile
			cu.is_operator = True
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
	cu.is_operator = False
	cu.save()
	return render(request,'logout.html')




