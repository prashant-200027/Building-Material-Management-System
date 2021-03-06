# Generated by Django 4.0.4 on 2022-04-19 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_alter_user_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='aadhar',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='aadharpic',
            field=models.FileField(blank=True, null=True, upload_to='AadharPic'),
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='district',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='pincode',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='pic',
            field=models.FileField(default='avtar.png', upload_to='profile'),
        ),
    ]
