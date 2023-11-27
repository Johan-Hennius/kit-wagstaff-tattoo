from django.db import models
from django.contrib.auth.models import User

COVER_UP_CHOICES = (
    ("Yes", "yes"),
    ("No", "No")
)

DAYS = (
    ("Wednesday", "wednesday"),
    ("Thursday", "thursday"),
    ("Friday", "friday"),
    ("Saturday", "saturday")
)

TIME = (
    ("Morning", "morning"),
    ("Afternoon", "afternoon")
)

COLOUR_OR = (
    ("Colour", "colour"),
    ("Black and Grey", "black and grey")
)

# Create your models here.
class Booking(models.Model):
    email_address = models.EmailField(max_length=300, unique=True)
    confirmed_day = models.DateField(null=True, blank=True)
    confirmed_time = models.TimeField(null=True, blank=True)
    preferred_day = models.CharField(choices=DAYS, default="Wednesday")
    preferred_time = models.CharField(choices=TIME, default="Morning")
    cover_up = models.CharField(choices=COVER_UP_CHOICES, default="No")
    color_or = models.CharField(choice=COLOR_OR, default="Colour")
    tattoo_location = models.CharField(max_length=75, default="Upper left arm")
    tattoo_description = models.TextField()
    terms = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.email_address}"