from django import forms
from django.forms import ModelForm
from .models import Booking

from cloudinary.forms import CloudinaryFileField

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = {
            'email_address',
            'preferred_day',
            'preferred_time',
            'cover_up',
            'color_or',
            'tattoo_location',
            'tattoo_description',
            'reference_images',
            'terms',
        }

        labels = {
            'email_address': '',
            'preferred_day': '',
            'preferred_time': 'Your preferred time',
            'cover_up': 'Is this a cover-up?',
            'color_or': 'Colour or black and grey',
            'tattoo_location': '',
            'tattoo_description': '',
            'reference_images': 'Reference images',
            'terms': 'I have read and agree to',
        }

        widgets = {
            'email_address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email address'}),
            'preferred_day': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Your preferred day'}),
            'preferred_time': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Your preferred time'}),
            'cover_up': forms.Select(attrs={'class': 'form-select',}),
            'color_or': forms.Select(attrs={'class': 'form-select',}),
            'tattoo_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Upper left arm'}),
            'tattoo_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Style, size, inspiration...'}),
            'reference_images': CloudinaryFileField(attrs={'class': 'form-control', 'placeholder': 'Style, size, inspiration...'}),
            'terms': forms.RadioSelect(attrs={'class': 'form-check-input'})
        }
