# Generated by Django 4.2.10 on 2024-05-11 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0013_category_page_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='page_url',
            field=models.CharField(default="{% url 'mobiles' %}", max_length=255),
        ),
    ]
