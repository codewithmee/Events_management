from django.shortcuts import render, HttpResponse
from .models import EventFacility,Members
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Eventhome(TemplateView):
    template_name = "event/eventfacility_Eventhome.html"

class EventRegistration(CreateView):
    model = EventFacility
    fields = ['org_name','Eventname','Esize','Evenue','Rooms','Foodfacility','Wifi']
    success_url = "/accounts/eventlist/"

    def get_success_url(self):
        if self.request.user.is_superuser:
            success_url = self.success_url
        else:
            success_url = "/thanks/"
        return success_url

class ThanksTemplateView(TemplateView):
    template_name = 'event/thanks.html'

class Eventmembers(LoginRequiredMixin,CreateView):
    model = Members
    fields = "__all__"
    template_name = "event/guest_form.html"
    success_url = "/accounts/eventlist/"
'''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ctg'] = EventRegistration.fields.all()
        return context'''

class LoginView(TemplateView):
    template_name = "event/login.html"


class ProfileView(LoginRequiredMixin,TemplateView,):
    template_name = "event/profile.html"

class EventList(LoginRequiredMixin,ListView):
    model = EventFacility
    context_object_name = "Events"
    template_name = "event/eventfacility_list.html"

    def get_queryset(self):
        return EventFacility.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(EventList, self).get_context_data(**kwargs)
        context['orgname']= EventFacility.objects.all().order_by('Esize')
        return context
 #no_use but for further projects
'''    def get_template_names(self):
        if self.request.user.is_superuser:
            template_name = self.template_name
        else:
            template_name = "event/blank.html"
        return [template_name]
'''

class EventDetailView(LoginRequiredMixin,DetailView):
    model = EventFacility
    template_name = "event/eventfacility_detail.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context['details']= Members.objects.filter(Organiser_Name_id=self.kwargs['pk']).order_by("memberName")
        return context

class EventUpdateView(LoginRequiredMixin,UpdateView,):
    login_url = 'accounts/login/'
    model = EventFacility
    fields = "__all__"
    success_url = "/accounts/eventlist/"

class GuestList(LoginRequiredMixin,ListView):
    model = Members
    context_object_name = "Guests"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GuestList, self).get_context_data(**kwargs)
        context['orderby'] = Members.objects.all().order_by("Organiser_Name")
        return context

class GuestDetailView(LoginRequiredMixin,DetailView):
    model = Members
    context_object_name = "members"

class GuestUpdateView(LoginRequiredMixin,UpdateView):
    model = Members
    fields = "__all__"
    template_name = "event/guest_form.html"
    success_url = "/accounts/guestlist/"

class LogoutView(LoginRequiredMixin,TemplateView):
    template_name = "registration/logged_out.html"

class PublishEvent(ListView):
    model= EventFacility
    template_name = "event/PublishedEvents.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PublishEvent, self).get_context_data(**kwargs)
        context['publish']= EventFacility.objects.all().filter(Publish=True)
        return context