# Generated by Django 5.1.4 on 2025-01-01 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0010_subjectdb_subject_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectdb',
            name='subject_id',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]