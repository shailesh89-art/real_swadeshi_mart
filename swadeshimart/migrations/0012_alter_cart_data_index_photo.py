# Generated by Django 4.2 on 2023-05-25 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swadeshimart', '0011_cart_data_index_photo_cart_data_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_data',
            name='index_photo',
            field=models.FileField(default=None, upload_to='cart_index'),
        ),
    ]
