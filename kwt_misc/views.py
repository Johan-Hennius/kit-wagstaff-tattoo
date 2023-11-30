from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def tattoo_care(request):
    return HttpResponse("Tattoo Care Page")


def terms(request):
    return HttpResponse("Terms & Conditions")


def contact(request):
    return HttpResponse("Contact")
