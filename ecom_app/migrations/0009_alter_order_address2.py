# Generated by Django 5.0.4 on 2024-05-01 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0008_remove_order_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address2',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
