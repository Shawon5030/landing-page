# Generated by Django 5.1.1 on 2025-03-25 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_order_customer_address_order_customer_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='mainPicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
