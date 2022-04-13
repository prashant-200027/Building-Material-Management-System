# Generated by Django 4.0.3 on 2022-04-08 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmms', '0018_rename_area_service_district_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='country',
            field=models.CharField(blank=True, choices=[('India', 'India'), ('Plumbing', 'Plumbing'), ('Painting', 'Painting'), ('Furniture', 'Furniture'), ('TextTile', 'TextTile')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='state',
            field=models.CharField(blank=True, choices=[('Gujarat', 'Gujarat'), ('Goa', 'Goa'), ('Delhi', 'Delhi'), ('Rajsthan', 'Rajsthan')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='district',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='typematerial',
            field=models.CharField(choices=[('Cement', 'Cement'), ('Plumbing', 'Plumbing'), ('Painting', 'Painting'), ('Furniture', 'Furniture'), ('TextTile', 'TextTile')], max_length=100),
        ),
    ]
