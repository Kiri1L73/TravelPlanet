# Generated by Django 3.2.16 on 2023-03-17 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20230317_2203'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductInBasket',
        ),
    ]