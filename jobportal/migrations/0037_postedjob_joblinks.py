# Generated by Django 4.0.5 on 2022-08-13 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0036_appliedjobs_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='postedjob',
            name='joblinks',
            field=models.CharField(default='', max_length=300),
        ),
    ]
