# Generated by Django 2.1.7 on 2019-04-16 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0011_auto_20190417_0011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='total_seats',
        ),
    ]
