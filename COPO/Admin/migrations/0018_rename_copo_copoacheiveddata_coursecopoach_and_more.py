# Generated by Django 5.1.4 on 2025-01-02 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0017_alter_subjectdb_subject_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='copoacheiveddata',
            old_name='copo',
            new_name='CourseCopoAch',
        ),
        migrations.RenameField(
            model_name='copoacheiveddata',
            old_name='data',
            new_name='CourseCopoAchExt',
        ),
        migrations.RenameField(
            model_name='copoacheiveddata',
            old_name='dataAch',
            new_name='copoAchExt',
        ),
    ]
