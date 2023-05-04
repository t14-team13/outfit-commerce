# Generated by Django 4.2 on 2023-05-04 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=40)),
                ('state', models.CharField(max_length=40)),
                ('number', models.CharField(max_length=40)),
                ('complement', models.CharField(default=None, max_length=40, null=True)),
                ('zipcode', models.CharField(max_length=40)),
            ],
        ),
    ]
