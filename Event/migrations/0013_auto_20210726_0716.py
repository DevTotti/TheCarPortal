# Generated by Django 3.2 on 2021-07-26 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0012_alter_eventvid_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='youtube',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='EventVid',
        ),
    ]
