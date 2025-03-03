# Generated by Django 5.1.4 on 2024-12-26 16:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_subjectdb_noco_subjectdb_nopo_subjectdb_nopso'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjectdb',
            name='CONAMES',
            field=models.JSONField(null=True),
        ),
        migrations.CreateModel(
            name='COPOAcheiveddata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('copo', models.JSONField(null=True)),
                ('data', models.JSONField(null=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.subjectdb', to_field='subject')),
            ],
        ),
        migrations.CreateModel(
            name='Corelationdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.JSONField(null=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.subjectdb', to_field='subject')),
            ],
        ),
        migrations.CreateModel(
            name='CourseExitdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('copo', models.JSONField(null=True)),
                ('data', models.JSONField(null=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.subjectdb', to_field='subject')),
            ],
        ),
    ]
