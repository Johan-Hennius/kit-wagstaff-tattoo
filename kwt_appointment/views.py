from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required

from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from django.contrib.auth.models import User

from django.views import generic
from django.contrib import messages

from .models import Booking
from .forms import BookingForm


@login_required
def create_booking(request):

    booking = BookingForm()

    if request.method == 'POST':
        form = BookingForm(request.POST, request.FILES)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.terms = True
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

    # user owns the booking - okay to proceed
    if request.method == "POST":
        form = BookingForm(request.POST or None, request.FILES, instance=booking)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.confirmed = False
            booking.terms = True
            form.save()
            messages.success(request, "Booking updated and awaiting approval")
            return redirect(reverse("my_bookings"))
        messages.error(request, "An error occured, please try again!")
    else:
        form = BookingForm(instance=booking)

    template = "bookings/update_booking.html"

    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def delete_booking(request, booking_id):
    """
    Functionality for a user to delete their own booking(s).
    """

    booking = get_object_or_404(Booking, id=booking_id)

    # user owns the booking - okay to proceed
    if booking.email_address != request.user:
        # not a match, take them back to their profile
        messages.error(request, "Access Denied. This is not your booking.")
        return redirect(reverse("my_bookings"))

    booking.delete()
    return redirect("my_bookings")
 


