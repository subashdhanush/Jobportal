# Generated by Django 4.0.5 on 2022-09-07 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0046_postedjob_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paypal_id', models.CharField(default=True, max_length=150)),
                ('payer_emailaddress', models.CharField(default='', max_length=200)),
                ('payer_id', models.CharField(default=True, max_length=150)),
                ('payee_emailaddress', models.CharField(default='', max_length=200)),
                ('currency_code', models.CharField(default=True, max_length=100)),
                ('amount', models.CharField(blank=True, max_length=150)),
                ('shippingaddress1', models.CharField(default='', max_length=700)),
                ('admin_area_1', models.CharField(default='', max_length=400)),
                ('admin_area_2', models.CharField(default='', max_length=400)),
                ('country_code', models.CharField(default='', max_length=400)),
                ('postal_code', models.CharField(default='', max_length=400)),
            ],
        ),
    ]
