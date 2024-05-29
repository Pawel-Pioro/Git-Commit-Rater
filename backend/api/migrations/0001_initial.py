# Generated by Django 5.0.6 on 2024-05-29 06:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=1024)),
                ('scenario', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='CommitMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commit_message', models.CharField(max_length=1024)),
                ('rate', models.IntegerField()),
                ('scenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.scenario')),
            ],
        ),
    ]