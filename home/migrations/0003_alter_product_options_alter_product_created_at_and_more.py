# Generated by Django 4.2 on 2023-04-27 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_alter_product_id"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ("-created_at",),
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.AlterField(
            model_name="product",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Когда создано"),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="product",
            name="img",
            field=models.ImageField(
                height_field="285",
                upload_to="uploads/products/img/",
                verbose_name="Изображение",
                width_field="285",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.FloatField(verbose_name="Цена"),
        ),
        migrations.AlterField(
            model_name="product",
            name="quantity",
            field=models.PositiveIntegerField(default=0, verbose_name="Количество"),
        ),
        migrations.AlterField(
            model_name="product",
            name="title",
            field=models.CharField(max_length=50, verbose_name="Название"),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Когда обновлено"),
        ),
    ]
