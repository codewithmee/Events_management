from django.urls import path,include
from event import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('profile/',views.ProfileView.as_view(),name="profile"),
    path('login/',views.LoginView.as_view(),name="login"),
    path('logout/',views.LogoutView.as_view(),name="logout"),
    path('eventlist/',views.EventList.as_view(), name="eventlist"),
    path('eventdetails/<slug:pk>',views.EventDetailView.as_view(),name="eventdetails"),
    path('guestdetails/<slug:pk>', views.GuestDetailView.as_view(), name="guestdetails"),
    path('eventupdate/<slug:pk>',views.EventUpdateView.as_view(), name="eventupdate"),
    path('guestlist/',login_required(views.GuestList.as_view()),name="guestslist"),
    path('guestupdate/<slug:pk>/',views.GuestUpdateView.as_view(),name="guestupdate"),
    path('addguest/',views.Eventmembers.as_view(),name="addguest"),
]