# Generated by Django 3.2.7 on 2021-12-31 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_auto_20211231_1130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventfacility',
            name='Publish',
        ),
    ]
