# Generated by Django 5.0.4 on 2024-10-21 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starter', '0002_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]
