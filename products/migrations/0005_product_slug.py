# Generated by Django 5.1 on 2024-08-19 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_active_product_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='slug_padrao'),
            preserve_default=False,
        ),
    ]