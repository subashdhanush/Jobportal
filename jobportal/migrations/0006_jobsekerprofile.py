# Generated by Django 4.0.5 on 2022-07-07 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0005_employeeprofile_employerid'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobsekerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(default='', max_length=150)),
                ('Qualification', models.CharField(default='', max_length=100)),
                ('fileupload', models.FileField(blank=True, default='', upload_to='store/pdfs')),
                ('jobcategory', models.CharField(default='True', max_length=50)),
                ('jobtype', models.CharField(default='', max_length=50)),
                ('joblevel', models.CharField(default='', max_length=50)),
                ('languages', models.CharField(default='', max_length=500)),
                ('salaryfrom', models.IntegerField(blank=True, default='1')),
                ('skills', models.CharField(default='', max_length=500)),
                ('experience', models.IntegerField(blank=True, default='1')),
                ('contactnumber', models.IntegerField(blank=True, default='1')),
                ('email', models.CharField(default='', max_length=150)),
                ('address', models.CharField(default='', max_length=500)),
                ('location', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
