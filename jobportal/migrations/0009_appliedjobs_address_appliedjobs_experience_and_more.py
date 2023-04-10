# Generated by Django 4.0.5 on 2022-07-08 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0008_appliedjobs'),
    ]

    operations = [
        migrations.AddField(
            model_name='appliedjobs',
            name='address',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='appliedjobs',
            name='experience',
            field=models.IntegerField(blank=True, default='1'),
        ),
        migrations.AddField(
            model_name='appliedjobs',
            name='skills',
            field=models.CharField(default='', max_length=500),
        ),
    ]