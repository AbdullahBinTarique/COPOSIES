# Generated by Django 5.1.4 on 2025-01-01 04:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0017_alter_subjectdb_subject_id'),
        ('Teachers', '0007_remove_teacher_subject_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='subject_id',
            field=models.ForeignKey(max_length=20, null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.subjectdb', to_field='subject_id'),
        ),
    ]
