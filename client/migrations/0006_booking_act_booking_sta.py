# Generated by Django 4.0.4 on 2022-04-26 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_booking_action_booking_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='act',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='sta',
            field=models.BooleanField(default=False),
        ),
    ]
