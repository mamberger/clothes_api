# Generated by Django 3.2.9 on 2022-12-18 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0019_auto_20221218_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telegramuser',
            name='favourites',
        ),
        migrations.AddField(
            model_name='item',
            name='subscribers',
            field=models.ManyToManyField(blank=True, null=True, to='items.TelegramUser'),
        ),
    ]
