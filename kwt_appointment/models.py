from django.db import models
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField

COVER_UP_CHOICES = (
    ("yes", "Yes"),
    ("no", "No")
)

DAYS = (
    ("wednesday", "Wednesday"),
    ("thursday", "Thursday"),
    ("friday", "Friday"),
    ("saturday", "Saturday")
)

TIME = (
    ("morning", "Morning"),
    ("afternoon", "Afternoon")
)

COLOR_OR = (
    ("colour", "Colour"),
    ("black and grey", "Black and Grey")
)


class Booking(models.Model):

    email_address = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="client_name",
        max_length=100
    )
    confirmed_day = models.DateField(null=True, blank=True)
    confirmed_time = models.TimeField(null=True, blank=True)
    preferred_day = models.CharField(choices=DAYS)
    preferred_time = models.CharField(choices=TIME)
    cover_up = models.CharField(choices=COVER_UP_CHOICES)
    color_or = models.CharField(choices=COLOR_OR)
    tattoo_location = models.CharField(max_length=75)
    tattoo_description = models.TextField()
    reference_images = CloudinaryField(
        "image",
        default="placeholder",
        null=True,
        blank=True
    )
    terms = models.BooleanField(default=True)
    confirmed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"This booking is for: {self.email_address} | Requested on: {self.created_on}"  # noqa
