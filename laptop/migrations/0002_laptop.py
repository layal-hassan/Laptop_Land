# Generated by Django 4.2.15 on 2024-08-26 17:07

from django.db import migrations, models
import laptop.models


class Migration(migrations.Migration):

    dependencies = [
        ('laptop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description1', models.TextField(max_length=4000)),
                ('image', models.ImageField(upload_to=laptop.models.image_upload)),
            ],
        ),
    ]
