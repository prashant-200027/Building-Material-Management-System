# Generated by Django 4.0.4 on 2022-04-24 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='action',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='status',
        ),
    ]
