# Generated by Django 4.0.4 on 2022-04-26 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_booking_act_booking_sta'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='ac',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='st',
            field=models.BooleanField(default=False),
        ),
    ]
