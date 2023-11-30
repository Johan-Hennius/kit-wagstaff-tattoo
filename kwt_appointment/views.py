from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from django.db.models import Q

from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponse

from .models import Booking
from .forms import BookingForm

# Create your views here.
# def booking_form(request):

#     if request.method == "POST":
#         booking_form = BookingForm(data=request.POST)
#         if booking_form.is_valid():
#             booking = booking_form.save(commit=False)
#             booking.approved = False
#             booking_form.save()
#             messages.add_message(
#                 request, messages.SUCCESS,
#                 "Booking submitted and awaiting approval"
#             )

#     booking_form = BookingForm

#     return render(
#         request,
#         'bookings/booking.html',
#         {
#             "booking_form": booking_form,
#         }
#     )

class CreateBooking(LoginRequiredMixin, CreateView):
    
    template_name = 'bookings/booking.html'
    model = Booking
    success_url = 'bookings/my_bookings.html'
    form_class = BookingForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateBooking, self).form_valid(form)


def my_bookings(request):
    return HttpResponse("My Bookings")