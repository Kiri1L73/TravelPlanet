# Generated by Django 3.2.16 on 2023-03-15 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=64, null=True),
        ),
    ]
