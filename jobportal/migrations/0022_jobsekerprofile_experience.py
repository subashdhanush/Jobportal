# Generated by Django 4.0.5 on 2022-08-04 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0021_remove_jobsekerprofile_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobsekerprofile',
            name='experience',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
