# Generated by Django 4.0.3 on 2022-04-07 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmms', '0014_user_country_user_state_alter_user_aadhar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='proof',
            field=models.FileField(blank=True, null=True, upload_to='idpic'),
        ),
    ]