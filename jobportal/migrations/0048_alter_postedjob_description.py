# Generated by Django 4.0.5 on 2022-09-15 14:06

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0047_payment_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postedjob',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]