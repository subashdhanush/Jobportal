# Generated by Django 4.0.5 on 2022-08-04 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0019_alter_postedjob_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='postedjob',
            name='deleteflag',
            field=models.IntegerField(default='0'),
        ),
    ]
