# Generated by Django 3.1.7 on 2021-10-20 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Feedapp', '0013_auto_20211020_1655'),
        ('Employee', '0004_auto_20211020_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeprofile',
            name='department',
            field=models.ForeignKey(default='OT', on_delete=django.db.models.deletion.DO_NOTHING, to='Feedapp.department'),
        ),
    ]