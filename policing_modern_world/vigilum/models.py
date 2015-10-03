from django.db import models
from django.contrib.auth.models import User
import binascii


class ut(models.Model):
    user = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.user

def hash_username(username):
    a = binascii.crc32(username)
    return a

class PoliceOfficer(models.Model):
    user = models.OneToOneField(User)
    username = models.CharField(max_length=300)
    is_operator = models.BooleanField(default=False)
    last_accessed = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.username

User.profile = property(lambda u: PoliceOfficer.objects.get_or_create(user=u,defaults={'username':u.username})[0])

class Record(models.Model):
    police = models.ForeignKey(PoliceOfficer, limit_choices_to={'is_operator':False})
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.police

class Crime(models.Model):
    CRIME_TYPE = (
        (1, 'Robbery'),
        (2, 'Theft'),
        (3, 'Rape'),
    )
    types = models.IntegerField(choices=CRIME_TYPE)
    address = models.CharField(max_length=300)
    isResolved = models.BooleanField(default=False)
    callerName = models.CharField(max_length=300)
    police = models.ForeignKey(PoliceOfficer, limit_choices_to={'is_operator':False}, null = True, blank = True)
    timestamp = models.DateTimeField(auto_now_add=True)
    coordinates = models.TextField(max_length=200)

    def __unicode__(self):
        return self.address
