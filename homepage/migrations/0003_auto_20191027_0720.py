# Generated by Django 2.2.2 on 2019-10-27 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20191027_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='category',
            field=models.CharField(choices=[('soil', 'Soil'), ('water', 'Water'), ('air', 'Air'), ('light', 'Light')], default='soil', max_length=6),
        ),
    ]
