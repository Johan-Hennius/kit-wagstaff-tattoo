from django.contrib import admin
from .models import Gallery


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):

    list_display = "title", "slug", "created_on"
    search_fields = ["title"]
    list_filter = ("title", "created_on",)
    prepopulated_fields = {"slug": ("title",)}
