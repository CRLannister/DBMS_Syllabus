# Generated by Django 2.2.3 on 2019-08-19 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_entry_masters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='subject_type',
            field=models.CharField(choices=[('Compulsory', 'Compulsory'), ('Elective', 'Elective')], default='COMPULSORY', max_length=20),
        ),
    ]