# Generated by Django 5.0.4 on 2024-05-01 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='serial_number',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
