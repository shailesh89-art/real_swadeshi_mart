# Generated by Django 4.2 on 2023-05-09 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swadeshimart', '0002_product_upload_database_delete_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='login_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logged_as', models.CharField(max_length=20)),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('date_of_birth', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('confirm_password', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
            ],
        ),
    ]