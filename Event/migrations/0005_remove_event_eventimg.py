# Generated by Django 3.2 on 2021-05-19 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0004_auto_20210519_0721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='eventImg',
        ),
    ]
