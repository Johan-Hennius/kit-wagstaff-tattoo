# Generated by Django 4.2.1 on 2023-12-01 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kwt_appointment', '0006_alter_booking_color_or_alter_booking_cover_up_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='terms',
            field=models.BooleanField(default=True),
        ),
    ]