# Generated by Django 2.1.7 on 2019-04-11 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0007_students_attendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='clgId',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]