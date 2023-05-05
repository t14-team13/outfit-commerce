# Generated by Django 4.2 on 2023-05-05 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("carts", "0002_initial"),
        ("orders", "0003_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="cart",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="cart_orders",
                to="carts.cart",
            ),
        ),
    ]
