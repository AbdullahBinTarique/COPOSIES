# Generated by Django 5.1.4 on 2024-12-31 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0008_remove_conames_id_remove_corelationdata_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminusers',
            name='slug',
            field=models.SlugField(max_length=20, unique=True),
        ),
    ]