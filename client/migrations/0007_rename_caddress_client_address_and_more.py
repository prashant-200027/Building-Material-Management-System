# Generated by Django 4.0.3 on 2022-04-07 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_client_cdistrict_client_cpincode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='caddress',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='ccountry',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='cdistrict',
            new_name='district',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='cemail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='cfname',
            new_name='fname',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='clname',
            new_name='lname',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='cmobile',
            new_name='mobile',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='cpassword',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='cpic',
            new_name='pic',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='cpincode',
            new_name='pincode',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='cstate',
            new_name='state',
        ),
    ]