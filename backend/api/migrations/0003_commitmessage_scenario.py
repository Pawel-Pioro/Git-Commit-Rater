# Generated by Django 4.2.4 on 2024-05-30 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_commitmessage_scenario'),
    ]

    operations = [
        migrations.AddField(
            model_name='commitmessage',
            name='scenario',
            field=models.IntegerField(null=True),
        ),
    ]