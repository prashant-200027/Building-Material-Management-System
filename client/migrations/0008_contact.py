# Generated by Django 4.0.3 on 2022-05-05 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_booking_ac_booking_st'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('subject', models.CharField(blank=True, max_length=30, null=True)),
                ('message', models.TextField()),
            ],
        ),
    ]
