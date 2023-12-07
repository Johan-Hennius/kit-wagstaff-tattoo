from django.shortcuts import render

from .models import Gallery


def gallery(request):

    images = Gallery.objects.all()
    context = {
        "images": images
    }

    return render(
        request,
        'gallery/gallery.html',
        context,
    )
