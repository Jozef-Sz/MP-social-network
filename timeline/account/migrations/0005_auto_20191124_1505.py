# Generated by Django 2.2.6 on 2019-11-24 14:05

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20191102_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='banner_picture',
            field=models.ImageField(blank=True, default='default_images/default_banner.jpg', upload_to=account.models.upload_banner_location),
        ),
        migrations.AlterField(
            model_name='account',
            name='profile_picture',
            field=models.ImageField(blank=True, default='default_images/default_profile.png', upload_to=account.models.upload_profile_location),
        ),
    ]
