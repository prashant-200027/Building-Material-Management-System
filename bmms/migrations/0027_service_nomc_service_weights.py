# Generated by Django 4.0.3 on 2022-04-08 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmms', '0026_service_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='nomc',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='weights',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]