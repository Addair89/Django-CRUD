# Generated by Django 5.0.3 on 2024-04-04 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_rename_owners_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='store',
            field=models.ManyToManyField(to='main_app.store'),
        ),
    ]
