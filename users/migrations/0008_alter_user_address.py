# Generated by Django 4.2 on 2023-05-03 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0007_remove_address_user'),
        ('users', '0007_user_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='address', to='addresses.address'),
        ),
    ]
