# Generated by Django 5.1.4 on 2025-01-01 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0012_alter_subjectdb_subject_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjectdb',
            name='subject_id',
        ),
    ]
