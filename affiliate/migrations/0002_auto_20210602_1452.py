# Generated by Django 3.2 on 2021-06-02 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affiliate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autodiagnosticimage',
            name='image',
            field=models.ImageField(upload_to='static/media/'),
        ),
        migrations.AlterField(
            model_name='autodiagnosticimage',
            name='video',
            field=models.FileField(upload_to='static/media/'),
        ),
        migrations.AlterField(
            model_name='carsaleimage',
            name='image',
            field=models.ImageField(upload_to='static/media/'),
        ),
        migrations.AlterField(
            model_name='carsaleimage',
            name='video',
            field=models.FileField(upload_to='static/media/'),
        ),
        migrations.AlterField(
            model_name='mechanicimage',
            name='image',
            field=models.ImageField(upload_to='static/media/'),
        ),
        migrations.AlterField(
            model_name='mechanicimage',
            name='video',
            field=models.FileField(upload_to='static/media/'),
        ),
        migrations.AlterField(
            model_name='spareimage',
            name='image',
            field=models.ImageField(upload_to='static/media/'),
        ),
        migrations.AlterField(
            model_name='spareimage',
            name='video',
            field=models.FileField(upload_to='static/media/'),
        ),
    ]
