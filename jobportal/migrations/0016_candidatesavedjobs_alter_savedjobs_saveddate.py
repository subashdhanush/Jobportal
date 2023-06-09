# Generated by Django 4.0.5 on 2022-07-14 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0015_alter_savedjobs_saveddate'),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateSavedJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobtitle', models.CharField(default='', max_length=100)),
                ('jobtype', models.CharField(default='', max_length=50)),
                ('status', models.CharField(default='', max_length=50)),
                ('username', models.CharField(default='', max_length=100)),
                ('email', models.CharField(default='', max_length=100)),
                ('companyname', models.CharField(default='', max_length=100)),
                ('flag', models.IntegerField(default='0')),
                ('employerid', models.CharField(default='0', max_length=50)),
                ('userid', models.CharField(default='0', max_length=50)),
                ('skills', models.CharField(default='', max_length=500)),
                ('saveddate', models.DateField(max_length=8)),
                ('expirydate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='savedjobs',
            name='saveddate',
            field=models.DateField(max_length=8),
        ),
    ]
