# Generated by Django 5.0.4 on 2024-04-29 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='catagory',
            field=models.CharField(default='cloths', max_length=255),
        ),
    ]
