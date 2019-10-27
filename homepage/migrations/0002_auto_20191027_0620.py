# Generated by Django 2.2.2 on 2019-10-27 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='category',
            field=models.CharField(choices=[('Soil', 'Soil'), ('Water', 'Water'), ('Air', 'Air'), ('Light', 'Light')], default='Soil', max_length=6),
        ),
        migrations.AlterField(
            model_name='picture',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='static/'),
        ),
    ]
