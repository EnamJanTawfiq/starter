# Generated by Django 5.0.4 on 2024-10-26 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starter', '0004_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
