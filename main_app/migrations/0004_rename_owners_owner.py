# Generated by Django 5.0.3 on 2024-04-03 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_owners'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Owners',
            new_name='Owner',
        ),
    ]
