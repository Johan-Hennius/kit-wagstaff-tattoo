from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about_kwt(request):
    return HttpResponse("About Page")