# Generated by Django 3.0.8 on 2020-07-30 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20200730_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetails',
            name='department',
            field=models.CharField(choices=[('Finance AND Accounts', 'Finance'), ('HR', 'HR'), ('Customer Care', 'Customer Care'), ('Store', 'Store'), ('Sales AND Marketing', 'Sales AND Marketing'), ('IT', 'IT'), ('Security', 'Security'), ('Cleaning', 'Cleaning'), ('Executive', 'Executive')], max_length=20),
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='email',
            field=models.EmailField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='job_title',
            field=models.CharField(choices=[('CEO', 'CEO'), ('Head', 'HEAD'), ('Manager', 'Manager'), ('Sr', 'Sr'), ('Accountant', 'Accountant'), ('Jnr', 'JUNIOR'), ('Guard', 'GUARD'), ('Consultant', 'Consultant')], max_length=20),
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
