# Generated by Django 2.2.2 on 2019-11-26 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_auto_20191120_0720'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='static/'),
        ),
    ]