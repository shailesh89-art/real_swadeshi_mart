# Generated by Django 4.2 on 2023-06-27 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swadeshimart', '0018_login_details_gender_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='address_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=15)),
                ('pincode', models.CharField(max_length=7)),
                ('locality', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=40)),
                ('landmark', models.CharField(max_length=150)),
                ('alternate_mobile', models.CharField(max_length=15)),
                ('address_location', models.CharField(max_length=10)),
            ],
        ),
    ]
