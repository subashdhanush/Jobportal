# Generated by Django 4.0.5 on 2022-08-04 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0025_remove_appliedjobs_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='appliedjobs',
            name='experience',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
