# Generated by Django 5.1.5 on 2025-02-04 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('content', models.TextField()),
                ('img_url', models.URLField(null=True)),
                ('craeted', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=500, unique=True)),
            ],
        ),
    ]
