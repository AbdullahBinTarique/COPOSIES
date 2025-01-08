# Generated by Django 5.1.4 on 2025-01-08 08:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0021_copoacheiveddata_uploade_date'),
        ('Teachers', '0010_alter_teacher_subject_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='copoacheiveddata',
            name='batch',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Teachers.batch'),
            preserve_default=False,
        ),
    ]
