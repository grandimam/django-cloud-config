# Generated by Django 5.1.2 on 2024-10-27 06:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('string', 'String'), ('hash', 'Hash'), ('list', 'List'), ('set', 'Set'), ('sorted_set', 'Sorted Set')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GlobalConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(help_text='Stores JSON for complex types like Hash, List, Set, and Sorted Set')),
                ('value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.configitem')),
            ],
        ),
    ]