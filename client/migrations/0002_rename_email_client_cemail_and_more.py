# Generated by Django 4.0.3 on 2022-04-07 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='email',
            new_name='cemail',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='fname',
            new_name='cfname',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='lname',
            new_name='clname',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='mobile',
            new_name='cmobile',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='password',
            new_name='cpassword',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='pic',
            new_name='cpic',
        ),
    ]
