from django.db import models
from django.urls import reverse

# Create your models here.

class EventFacility(models.Model):
    org_name = models.CharField(max_length=200,unique=True)
    Eventname = models.CharField(max_length=200)
    Esize = models.IntegerField()
    Evenue = models.CharField(max_length=200)
    Rooms = models.IntegerField()
    Foodfacility = models.BooleanField(default=False)
    Wifi = models.BooleanField(default=False)
    Publish = models.BooleanField(default=False)

    def get_absolte_url(self):
        return reverse('thanks')

    def __str__(self):
        s= self.org_name +" " +self.Eventname +" "+ "Event"
        return s

class Members(models.Model):
    Organiser_Name = models.ForeignKey(EventFacility,on_delete=models.CASCADE)
    memberName = models.CharField(max_length=100)
    contactNumber = models.IntegerField(unique=True)
    relation = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('guestslist')
