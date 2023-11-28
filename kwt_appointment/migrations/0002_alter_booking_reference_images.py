# Generated by Django 4.2.1 on 2023-11-28 20:13

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kwt_appointment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='reference_images',
            field=cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, null=True, verbose_name='image'),
        ),
    ]
