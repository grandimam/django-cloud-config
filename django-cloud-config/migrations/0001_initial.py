from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),

        migrations.CreateModel(
            name='ConfigVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=100)),
                ('config_data', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('data_source', models.CharField(choices=[('db', 'db'), ('vc', 'vc')], default='db', max_length=50)),
                ('github_repo_url', models.URLField(blank=True, null=True)),
                ('github_file_path', models.CharField(blank=True, max_length=255, null=True)),
                ('config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='your_app.Config')),
                ('environment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='your_app.Environment')),
            ],
        ),
    ]
