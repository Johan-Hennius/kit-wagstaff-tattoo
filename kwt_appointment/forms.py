from django import forms
from django.contrib.auth.models import User
from .models import Booking

from cloudinary.forms import CloudinaryFileField


class BookingForm(forms.ModelForm):

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
            'terms': '',
        }

        widgets = {
            'preferred_day': forms.Select(attrs={'class': 'form-select', }),
            'preferred_time': forms.Select(attrs={'class': 'form-select', }),
            'cover_up': forms.Select(attrs={'class': 'form-select', }),
            'color_or': forms.Select(attrs={'class': 'form-select', }),
            'tattoo_location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Upper left arm'
            }),
            'tattoo_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Style, size, inspiration...'
            }),
            'terms': forms.RadioSelect(attrs={'class': 'form-check-input'})
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
