# Generated by Django 2.2.3 on 2019-08-22 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_entry', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='syllabus',
            name='syllabus_name',
        ),
    ]
