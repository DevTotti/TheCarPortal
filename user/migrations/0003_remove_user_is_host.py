# Generated by Django 3.2 on 2021-06-02 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_host',
        ),
    ]
