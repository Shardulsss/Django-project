# Generated by Django 2.1.7 on 2019-04-08 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0006_auto_20190408_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='Attendance',
            field=models.BooleanField(default=False),
        ),
    ]