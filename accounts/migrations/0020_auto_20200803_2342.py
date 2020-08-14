# Generated by Django 3.0.8 on 2020-08-03 20:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20200730_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='date_employed',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='department',
            field=models.CharField(choices=[('Finance', 'Finance'), ('HR', 'HR'), ('Customer Care', 'Customer Care'), ('Store', 'Store'), ('Sales', 'Sales AND Marketing'), ('IT', 'IT'), ('Security', 'Security'), ('Cleaning', 'Cleaning'), ('Executive', 'Executive')], max_length=20),
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='salary',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='employeeprofile',
            name='date_employed',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
