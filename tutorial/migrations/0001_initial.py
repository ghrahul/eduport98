# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 14:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
                ('answer', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_type', models.CharField(max_length=10000000)),
                ('note_title', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutor', models.CharField(max_length=250)),
                ('subject_name', models.CharField(max_length=250)),
                ('Subject_area', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=250)),
                ('video_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutorial.Subject')),
            ],
        ),
        migrations.AddField(
            model_name='note',
            name='note_subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutorial.Subject'),
        ),
    ]
