# Generated by Django 5.0.4 on 2024-04-30 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0003_product_image_url_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=1000)),
                ('address2', models.CharField(max_length=1000)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('zipcode', models.CharField(max_length=255)),
            ],
        ),
    ]
