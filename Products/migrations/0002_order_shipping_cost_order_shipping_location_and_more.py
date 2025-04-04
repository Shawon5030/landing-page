# Generated by Django 5.1.2 on 2025-03-14 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping_cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_location',
            field=models.CharField(default='Outside Dhaka', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='total_with_charge',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
