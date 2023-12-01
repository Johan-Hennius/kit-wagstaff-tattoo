from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required

from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic
from django.contrib import messages

from .models import Booking
from .forms import BookingForm


# class CreateBooking(LoginRequiredMixin, CreateView):
    
#     template_name = 'bookings/booking.html'
#     model = Booking
#     success_url = '/booking/my-bookings/'
#     form_class = BookingForm

#     def form_valid(self, form):
#         form.instance.email_address = self.request.user
#         return super(CreateBooking, self).form_valid(form)


@login_required
def create_booking(request):

    booking = BookingForm()

    if request.method == 'POST':
        form = BookingForm(request.POST, request.FILES)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.email_address = request.user
            booking.save()
            messages.success(
                    request, 
                    "Booking created and awaiting approval"
                )
            return redirect('/booking/my-bookings/')
    else:
        form = BookingForm()

    return render(
        request,
        'bookings/booking.html',
        {
            "form": form
        }
    )



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



@login_required
def update_booking(request, booking_id):
    """
    Functionality for a user to update their own booking(s).
    """

    # grab the existing booking
    booking = get_object_or_404(Booking, id=booking_id)
    # check to see if the authenticated user owns this booking
    if booking.email_address != request.user:
        # not a match, take them back to their profile
        messages.error(request, "Access Denied. This is not your booking.")
        return redirect(reverse("my_bookings"))

    form = BookingForm(request.POST or None, request.FILES, instance=booking)

    # user owns the booking - okay to proceed
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Booking updated and awaiting approval")
            return redirect(reverse("my_bookings"))
        messages.error(request, "An error occured, please try again!")

    template = "bookings/booking.html"

    context = {
        "form": form,
    }

    return render(request, template, context)


class DeleteBooking(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Delete a booking
    """
    template_name = 'bookings/delete_booking.html'
    model = Booking
    success_url = '/booking/my-bookings/'
    

    def test_func(self):
        return self.request.user == self.get_object().email_address       


