# Generated by Django 4.2 on 2023-05-19 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swadeshimart', '0004_alter_login_details_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='login_details',
            name='cart',
            field=models.CharField(default=0, max_length=100),
        ),
    ]