# Generated by Django 4.0.5 on 2022-08-10 12:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0031_jobsekerprofile_singaporean'),
    ]

    operations = [
        migrations.AddField(
            model_name='postedjob',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]