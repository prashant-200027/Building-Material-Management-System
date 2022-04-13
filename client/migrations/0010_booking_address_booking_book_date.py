# Generated by Django 4.0.3 on 2022-04-11 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0009_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='book_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
