# Generated by Django 3.1.7 on 2021-10-20 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0003_auto_20211006_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeprofile',
            name='desg',
            field=models.TextField(blank=True, choices=[('GM', 'General Manager'), ('SM', 'Senior Manager'), ('MR', 'Manager'), ('SE', 'Senior Engineer'), ('ER', 'Engineer'), ('MC', 'Master Craftsman'), ('CO', 'Consultant'), ('GE', 'Graduate Engineer Trainee'), ('DE', 'Diploma Engineer Trainee'), ('OJ', 'On Job Trainee')], max_length=10, verbose_name='Designation'),
        ),
        migrations.AddField(
            model_name='employeeprofile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='Employee_Photos'),
        ),
        migrations.AddField(
            model_name='employeeprofile',
            name='qual',
            field=models.TextField(blank=True, max_length=20, verbose_name='Qualification'),
        ),
    ]
