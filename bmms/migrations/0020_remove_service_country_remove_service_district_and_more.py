# Generated by Django 4.0.3 on 2022-04-08 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmms', '0019_service_country_service_state_alter_service_district_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='country',
        ),
        migrations.RemoveField(
            model_name='service',
            name='district',
        ),
        migrations.RemoveField(
            model_name='service',
            name='price',
        ),
        migrations.RemoveField(
            model_name='service',
            name='state',
        ),
        migrations.AlterField(
            model_name='service',
            name='proddesc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
