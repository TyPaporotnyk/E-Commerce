# Generated by Django 4.2.3 on 2023-08-09 13:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cart", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="cartproduct",
            name="quantity",
            field=models.PositiveIntegerField(default=1, max_length=1000),
        ),
    ]
