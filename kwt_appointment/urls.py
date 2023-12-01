from django.urls import path
from .views import my_bookings, UpdateBooking, DeleteBooking, create_booking

urlpatterns = [
    path("", create_booking, name="booking_form"),
    path("my-bookings/", my_bookings, name="my_bookings"),
    path("delete-booking/<slug:pk>", DeleteBooking.as_view(), name="delete_booking"),
    path("update-booking/<slug:pk>", UpdateBooking.as_view(), name="update_booking"),
]