# Generated by Django 5.0.4 on 2024-05-01 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0006_order_items_order_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.CharField(max_length=255),
        ),
    ]
