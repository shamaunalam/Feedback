# Generated by Django 3.0.2 on 2021-10-06 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=50)),
            ],
        ),
    ]
