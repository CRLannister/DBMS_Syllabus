# Generated by Django 2.2.3 on 2019-08-16 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_entry', '0013_auto_20190805_1222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('level_id', models.AutoField(primary_key=True, serialize=False)),
                ('level_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Level',
            },
        ),
        migrations.RemoveField(
            model_name='subject',
            name='syllabus',
        ),
        migrations.AddField(
            model_name='syllabus',
            name='Subject',
            field=models.ManyToManyField(to='data_entry.Subject'),
        ),
    ]