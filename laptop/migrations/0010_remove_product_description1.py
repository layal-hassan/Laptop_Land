# Generated by Django 4.2.15 on 2024-09-30 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laptop', '0009_category_accessorym_name2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description1',
        ),
    ]
