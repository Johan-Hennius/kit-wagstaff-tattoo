from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponse

from .models import Booking
from .forms import BookingForm


class CreateBooking(LoginRequiredMixin, CreateView):
    
    template_name = 'bookings/booking.html'
    model = Booking
    success_url = '/booking/my-bookings/'
    form_class = BookingForm

    def form_valid(self, form):
        form.instance.email_address = self.request.user
        return super(CreateBooking, self).form_valid(form)


def my_bookings(request):
    user_profile = request.user
    approved_bookings = Booking.objects.filter(email_address = request.user, confirmed=True)
    pending_bookings = Booking.objects.filter(email_address = request.user, confirmed=False)
    
    return render(
        request, 
        'bookings/my_bookings.html',
        {
            'approved_bookings': approved_bookings,
            'pending_bookings': pending_bookings,
        }
    )


class UpdateBooking(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Update a booking
    """
    template_name = 'bookings/update_booking.html'
    model = Booking
    form_class = BookingForm
    success_url = '/booking/my-bookings/'

    def test_func(self):
        return self.request.user == self.get_object().email_address


class DeleteBooking(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Delete a booking
    """
    template_name = 'bookings/delete_booking.html'
    model = Booking
    success_url = '/booking/my-bookings/'
    

    def test_func(self):
        return self.request.user == self.get_object().email_address       