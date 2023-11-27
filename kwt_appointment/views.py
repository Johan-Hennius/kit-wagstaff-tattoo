from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def booking_form(request):
    return HttpResponse("Booking Form")


def my_bookings(request):
    return HttpResponse("My Bookings")