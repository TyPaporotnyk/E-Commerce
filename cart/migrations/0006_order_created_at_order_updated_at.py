# Generated by Django 4.2 on 2023-05-11 20:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0005_customeraddress_remove_customer_city_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Дата создания",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="order",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Дата обновления"),
        ),
    ]