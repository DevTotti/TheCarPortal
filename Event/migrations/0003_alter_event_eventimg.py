# Generated by Django 3.2 on 2021-05-13 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0002_event_venue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='eventImg',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
