# Generated by Django 4.0.3 on 2022-04-08 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmms', '0025_service_mimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
