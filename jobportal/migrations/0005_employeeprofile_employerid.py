# Generated by Django 4.0.5 on 2022-07-06 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0004_employeedetails_employeeprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeprofile',
            name='employerid',
            field=models.CharField(default='0', max_length=50),
        ),
    ]