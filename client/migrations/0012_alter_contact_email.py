# Generated by Django 4.0.3 on 2022-05-05 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0011_remove_contact_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
