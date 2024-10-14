# Generated by Django 4.2.15 on 2024-09-07 05:27

from django.db import migrations, models
import laptop.models


class Migration(migrations.Migration):

    dependencies = [
        ('laptop', '0003_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('image', models.ImageField(upload_to=laptop.models.image_upload)),
            ],
        ),
    ]
