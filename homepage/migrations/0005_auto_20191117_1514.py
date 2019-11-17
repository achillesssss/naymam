# Generated by Django 2.2.2 on 2019-11-17 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20191117_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='author',
        ),
        migrations.AddField(
            model_name='picture',
            name='album',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='homepage.Album'),
        ),
    ]
