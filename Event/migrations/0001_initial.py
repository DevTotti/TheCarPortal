# Generated by Django 3.2 on 2021-05-09 17:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('status', models.CharField(blank=True, choices=[('P', 'Past'), ('U', 'Upcoming')], default='U', max_length=10)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('description', models.CharField(max_length=300)),
                ('full_details', models.TextField(blank=True)),
                ('eventImg', models.ImageField(upload_to='')),
            ],
        ),
    ]
