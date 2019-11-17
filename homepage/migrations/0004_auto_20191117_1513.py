# Generated by Django 2.2.2 on 2019-11-17 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20191027_0720'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('link', models.TextField(blank=True, null=True)),
            ],
        ),
        # migrations.RemoveField(
        #     model_name='picture',
        #     name='author',
        # ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Author')),
            ],
        ),
        # migrations.AddField(
        #     model_name='picture',
        #     name='album',
        #     field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='homepage.Album'),
        # ),
    ]
