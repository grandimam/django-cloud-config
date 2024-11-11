# django-cloud-config

Django Cloud Config

### Creating Config Versions

```
# Create an environment (e.g., development)
dev_env = Environment.objects.create(name='development', description='Development environment')

# Create a configuration (e.g., database config)
db_config = Config.objects.create(name='database_config', description='Configuration for the database')

# Create a version for the database config (stored in DB)
dev_db_version = ConfigVersion(config=db_config, environment=dev_env, version='v1', data_source='db')
dev_db_version.save_config({
    'database': {
        'host': 'localhost',
        'port': 5432,
        'user': 'dev_user',
        'password': 'dev_password'
    }
})

# Create a version for the database config (stored in GitHub)
dev_db_github_version = ConfigVersion(
    config=db_config, environment=dev_env, version='v2', data_source='github',
    github_repo_url='https://github.com/your-org/your-repo',
    github_file_path='config/dev_db_config.yaml',
)
dev_db_github_version.fetch_config_from_github()  # Fetch and store config from GitHub
```