# Generated by Django 4.0.5 on 2022-08-09 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0029_employeecontact_empaddress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobsekerprofile',
            name='joblevel',
        ),
        migrations.RemoveField(
            model_name='jobsekerprofile',
            name='languages',
        ),
        migrations.RemoveField(
            model_name='jobsekerprofile',
            name='location',
        ),
        migrations.RemoveField(
            model_name='jobsekerprofile',
            name='skills',
        ),
    ]
