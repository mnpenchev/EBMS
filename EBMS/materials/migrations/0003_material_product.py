# Generated by Django 5.0.4 on 2024-05-09 07:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_alter_material_serial_number'),
        ('products', '0003_remove_product_materials'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
