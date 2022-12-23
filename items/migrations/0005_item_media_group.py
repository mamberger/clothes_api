# Generated by Django 3.2.9 on 2022-11-27 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_mediafile'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='media_group',
            field=models.ManyToManyField(related_name='media', to='items.MediaFile'),
        ),
    ]
