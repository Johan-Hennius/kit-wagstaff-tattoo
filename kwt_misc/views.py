from django.shortcuts import render
from django.http import HttpResponse


def tattoo_care(request):
    return render(
        request,
        "misc/tattoo_care.html",
        {
        }
    )


def terms(request):
    return render(
        request,
        "misc/terms.html",
        {
        }
    )
