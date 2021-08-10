# Generated by Django 3.2 on 2021-08-10 07:43

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('exterior_color', models.CharField(max_length=200)),
                ('interior_color', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('type_of_car', models.CharField(choices=[('Sedan', 'Sedan'), ('SUV', 'SUV'), ('Truck', 'Truck')], max_length=200)),
                ('engine_type', models.CharField(choices=[('V6', 'V6'), ('V12', 'V12'), ('V8', 'V8')], max_length=200)),
                ('drive_train', models.CharField(choices=[('AWD', 'AWD'), ('FWD', 'FWD'), ('4WD', '4WD')], max_length=200)),
                ('fuel_type', models.CharField(choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Electric', 'Electric')], max_length=200)),
                ('faults', models.TextField(blank=True)),
                ('make', models.CharField(max_length=200)),
                ('man_year', models.DateField()),
                ('registered', models.BooleanField(default=False)),
                ('registration_number', models.CharField(default='', max_length=10)),
                ('distance_covered', models.IntegerField()),
                ('transmission', models.CharField(choices=[('AUTO', 'Authomatic'), ('MANUAL', 'Manual')], max_length=200)),
                ('usage_type', models.CharField(choices=[('Tokunbo', 'Tokunbo'), ('Nigerian-Used', 'Nigerian-Used')], default='', max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(choices=[('Ife', 'Ile-Ife'), ('Ibadan', 'Ibadan'), ('Lagos', 'Lagos')], max_length=200)),
                ('video', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='video')),
            ],
        ),
        migrations.CreateModel(
            name='CarSaleImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('width', models.FloatField(default=100)),
                ('length', models.FloatField(default=100)),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Automart.carsale')),
            ],
        ),
    ]
