# Generated by Django 3.2.9 on 2022-11-27 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0008_alter_item_media_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='media_group',
        ),
        migrations.AddField(
            model_name='item',
            name='media_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='items.mediafile'),
        ),
    ]
