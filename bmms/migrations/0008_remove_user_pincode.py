# Generated by Django 4.0.3 on 2022-04-07 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bmms', '0007_user_pincode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='pincode',
        ),
    ]
