# Generated by Django 5.1.4 on 2025-01-08 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0024_alter_copoacheiveddata_batch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='copoacheiveddata',
            name='batch',
        ),
    ]
