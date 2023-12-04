from django.contrib import admin
from .models import Gallery


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):

    list_display = "title", "created_on"
    search_fields = ["title"]
    list_filter = ("title", "created_on",)
