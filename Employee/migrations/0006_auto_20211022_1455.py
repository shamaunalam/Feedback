# Generated by Django 3.1.7 on 2021-10-22 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0005_employeeprofile_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeprofile',
            name='photo',
            field=models.ImageField(default='Employee_Photos/default_photo.png', upload_to='Employee_Photos'),
        ),
    ]
