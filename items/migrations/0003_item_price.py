# Generated by Django 3.2.9 on 2022-11-27 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_item_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, default=500, max_digits=7),
            preserve_default=False,
        ),
    ]
