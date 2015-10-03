from django.db import models
from datetime import datetime
from django.contrib.auth.signals import user_logged_in, user_logged_out  
from django.contrib.auth.models import User
import urllib, hashlib, binascii

class ut(models.Model):
	user = models.CharField(max_length=200)
	time = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.user

def hash_username(username):
	a = binascii.crc32(username)
	return a
class Userc(models.Model):
	user = models.OneToOneField(User)
	userID =  models.IntegerField()
	username = models.CharField(max_length=300)
	is_user = models.BooleanField(default=False)
	last_accessed = models.DateTimeField(auto_now_add=True)
	
User.profile = property(lambda u: Userc.objects.get_or_create(user=u,defaults={'username':u.username,'userID':hash_username(u.username)})[0])
