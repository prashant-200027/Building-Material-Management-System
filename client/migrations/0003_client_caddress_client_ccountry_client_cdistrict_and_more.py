# Generated by Django 4.0.3 on 2022-04-07 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_rename_email_client_cemail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='caddress',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='ccountry',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='cdistrict',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='cpincode',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='cstate',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]