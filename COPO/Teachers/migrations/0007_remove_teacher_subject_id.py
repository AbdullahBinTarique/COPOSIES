# Generated by Django 5.1.4 on 2025-01-01 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Teachers', '0006_alter_teacher_subject_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='subject_id',
        ),
    ]
