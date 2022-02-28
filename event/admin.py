from django.contrib import admin
from .models import EventFacility,Members
# Register your models here.

@admin.register(EventFacility)

class EventFacilityAdmin(admin.ModelAdmin):
    list_display = ['id','org_name','Eventname','Esize','Evenue','Rooms','Foodfacility','Wifi','Publish']

class EventMembers(admin.ModelAdmin):
    list_display = ['id','Organiser_Name','memberName','contactNumber','relation']

admin.site.register(Members,EventMembers)
