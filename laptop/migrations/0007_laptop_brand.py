# Generated by Django 4.2.15 on 2024-09-25 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laptop', '0006_category_accessoryl_category_accessorym_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='laptop.brand'),
            preserve_default=False,
        ),
    ]
