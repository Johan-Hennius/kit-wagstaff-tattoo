from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        'email_address',
        'created_on',
        'confirmed_day',
        'confirmed_time',
        'confirmed'
    )
    search_fields = ['email_address', 'confirmed_day']
    list_filter = ('confirmed', 'created_on',)
