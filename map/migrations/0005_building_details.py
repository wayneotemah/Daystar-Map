# Generated by Django 4.0.1 on 2022-01-08 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_event_current_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='details',
            field=models.TextField(default='more details'),
            preserve_default=False,
        ),
    ]
