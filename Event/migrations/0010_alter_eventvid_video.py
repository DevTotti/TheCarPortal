# Generated by Django 3.2 on 2021-07-21 06:39

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0009_auto_20210721_0615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventvid',
            name='video',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='auto'),
        ),
    ]
