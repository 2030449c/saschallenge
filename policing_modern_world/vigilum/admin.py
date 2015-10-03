from django.contrib import admin
from vigilum.models import PoliceOfficer, Record, Crime, Message

class PoliceOfficerAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_operator']

class RecordAdmin(admin.ModelAdmin):
    list_display = ['police', 'timestamp']

class CrimeAdmin(admin.ModelAdmin):
    list_display = ['type', 'address', 'timestamp', 'callerName']

class MessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'message', 'time']

admin.site.register(PoliceOfficer, PoliceOfficerAdmin)
admin.site.register(Record, RecordAdmin)
admin.site.register(Crime, CrimeAdmin)
admin.site.register(Message, MessageAdmin)
