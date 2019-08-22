# Generated by Django 2.2.3 on 2019-08-18 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_id', models.AutoField(primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Department',
            },
        ),
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
        migrations.CreateModel(
            name='Program',
            fields=[
                ('program_id', models.AutoField(primary_key=True, serialize=False)),
                ('program_name', models.CharField(max_length=200)),
                ('program_short_name', models.CharField(max_length=30, null=True)),
                ('dept_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_entry_masters.Department')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_entry_masters.Level')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject_code', models.CharField(max_length=25)),
                ('subject_name', models.CharField(max_length=100)),
                ('credit', models.IntegerField(blank=True, null=True)),
                ('internal', models.IntegerField(blank=True, null=True)),
                ('external', models.IntegerField(blank=True, null=True)),
                ('total', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('syllabus_id', models.AutoField(primary_key=True, serialize=False)),
                ('syllabus_name', models.CharField(help_text='BCT_I_I_Part', max_length=50)),
                ('year', models.IntegerField()),
                ('part', models.IntegerField()),
                ('total_final_marks', models.IntegerField()),
                ('Subject', models.ManyToManyField(to='data_entry_masters.Subject')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_entry_masters.Program')),
            ],
            options={
                'verbose_name_plural': 'Syllabus',
            },
        ),
    ]