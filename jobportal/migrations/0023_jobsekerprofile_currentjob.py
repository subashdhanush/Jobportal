# Generated by Django 4.0.5 on 2022-08-04 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0022_jobsekerprofile_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobsekerprofile',
            name='currentjob',
            field=models.CharField(default='', max_length=150),
        ),
    ]
