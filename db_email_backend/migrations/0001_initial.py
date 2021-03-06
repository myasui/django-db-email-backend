# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-03 18:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('subject', models.TextField(blank=True)),
                ('body', models.TextField(blank=True)),
                ('content_subtype', models.CharField(max_length=254)),
                ('from_email', models.CharField(blank=True, max_length=254)),
                ('to', models.TextField(blank=True)),
                ('cc', models.TextField(blank=True)),
                ('bcc', models.TextField(blank=True)),
                ('headers', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmailAlternative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True)),
                ('mimetype', models.CharField(blank=True, max_length=254)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alternatives', to='db_email_backend.Email')),
            ],
        ),
        migrations.CreateModel(
            name='EmailAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(blank=True, max_length=1000)),
                ('mimetype', models.CharField(blank=True, max_length=254)),
                ('file', models.FileField(upload_to='db_email_backend')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='db_email_backend.Email')),
            ],
        ),
    ]
