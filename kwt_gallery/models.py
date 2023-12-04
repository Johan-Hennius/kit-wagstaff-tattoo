from django.db import models

from cloudinary.models import CloudinaryField


class Gallery(models.Model):
    title = models.CharField(max_length=150, unique=True)
    gallery_image = CloudinaryField('image', default='placeholder')
    caption = models.CharField(max_length=300, default="Please write your caption here...")
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Title: {self.title} | Uploaded: {self.created_on}"