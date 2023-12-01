from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Booking

from cloudinary.forms import CloudinaryFileField

class BookingForm(ModelForm):

    class Meta:
        model = Booking
        fields = {
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
            'preferred_day': 'Preferred day',
            'preferred_time': 'Your preferred time',
            'cover_up': 'Is this a cover-up?',
            'color_or': 'Colour or black and grey',
            'tattoo_location': 'Tattoo Location',
            'tattoo_description': 'Tattoo Description',
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
    }

    field_order = [
        'preferred_day',
        'preferred_time',
        'cover_up',
        'color_or',
        'tattoo_location',
        'tattoo_description',
        'reference_images',
        'terms',    
    ]

    

