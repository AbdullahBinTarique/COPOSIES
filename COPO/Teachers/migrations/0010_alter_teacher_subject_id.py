# Generated by Django 5.1.4 on 2025-01-01 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teachers', '0009_alter_teacher_subject_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='subject_id',
            field=models.CharField(default='Subject', max_length=20),
        ),
    ]