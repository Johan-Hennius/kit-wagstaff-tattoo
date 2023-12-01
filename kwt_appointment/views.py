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
        form = BookingForm(data=request.POST)
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



def update_booking(Booking, booking_id):

    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == 'POST':
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

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