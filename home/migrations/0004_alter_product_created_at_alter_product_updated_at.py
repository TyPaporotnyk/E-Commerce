# Generated by Django 4.2 on 2023-05-11 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_product_brand"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Дата создания"),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Дата обновления"),
        ),
    ]
