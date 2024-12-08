# Generated by Django 5.1.2 on 2024-11-06 20:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUSERS',
            fields=[
                ('email', models.CharField(default='name@gmail/sies.edu.in', max_length=100, primary_key=True, serialize=False, unique=True)),
                ('usertype', models.CharField(default='TE', max_length=2)),
                ('password', models.CharField(default='Password', max_length=15)),
                ('fname', models.CharField(default='FirstName', max_length=10)),
                ('lname', models.CharField(default='LastName', max_length=10)),
                ('username', models.CharField(default='UserName', max_length=15)),
                ('sem', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)])),
                ('slug', models.SlugField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectDB',
            fields=[
                ('srno', models.AutoField(primary_key=True, serialize=False)),
                ('object_id', models.PositiveIntegerField()),
                ('COs', models.TextField()),
            ],
        ),
    ]
