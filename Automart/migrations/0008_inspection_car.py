# Generated by Django 3.2 on 2021-08-18 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Automart', '0007_auto_20210810_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspection',
            name='car',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booked_inspection', to='Automart.carsale'),
        ),
    ]
