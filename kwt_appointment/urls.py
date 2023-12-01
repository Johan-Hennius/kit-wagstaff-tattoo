from django.urls import path
from .views import my_bookings, update_booking, DeleteBooking, create_booking

urlpatterns = [
    path("", create_booking, name="booking_form"),
    path("my-bookings/", my_bookings, name="my_bookings"),
    path("delete-booking/<slug:pk>", DeleteBooking.as_view(), name="delete_booking"),
    path("update-booking/<int:booking_id>", update_booking, name="update_booking"),
]