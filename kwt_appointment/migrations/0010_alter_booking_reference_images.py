# Generated by Django 4.2.1 on 2023-12-06 10:20

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kwt_appointment', '0009_alter_booking_color_or_alter_booking_cover_up_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='reference_images',
            field=cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, null=True, verbose_name='image'),
        ),
    ]
