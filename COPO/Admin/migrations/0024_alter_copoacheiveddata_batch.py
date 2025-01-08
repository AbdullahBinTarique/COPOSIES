# Generated by Django 5.1.4 on 2025-01-08 08:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0023_alter_copoacheiveddata_batch'),
        ('Teachers', '0010_alter_teacher_subject_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='copoacheiveddata',
            name='batch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Teachers.batch'),
        ),
    ]
