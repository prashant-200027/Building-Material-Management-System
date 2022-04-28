# Generated by Django 4.0.4 on 2022-04-19 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('seller', '0005_service_acitive'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('pic', models.FileField(default='avtar.png', upload_to='Clientprofile')),
                ('country', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=10)),
                ('district', models.CharField(max_length=20)),
                ('pincode', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_date', models.DateField(blank=True, null=True)),
                ('amount', models.IntegerField(default=0)),
                ('address', models.TextField(blank=True, null=True)),
                ('pay_id', models.CharField(blank=True, max_length=30, null=True)),
                ('verify', models.BooleanField(default=False)),
                ('pay_at', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=False)),
                ('action', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.clientuser')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.service')),
            ],
        ),
    ]
