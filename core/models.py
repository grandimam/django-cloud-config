import yaml
import requests
from django.db import models
from django.conf import settings

DATABASE = 'db'
VERSION_CONTROL = 'vc'


class Environment(models.Model):
    """Model to store different environments."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Config(models.Model):
    """Model to store configuration metadata."""
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class ConfigVersion(models.Model):
    """Model to store versions of a configuration for a specific environment."""
    config = models.ForeignKey(Config, on_delete=models.CASCADE)
    environment = models.ForeignKey(Environment, on_delete=models.CASCADE)
    version = models.CharField(max_length=100)
    config_data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    data_source = models.CharField(max_length=50, choices=['db', 'vc'], default='db')
    github_repo_url = models.URLField(blank=True, null=True)
    github_file_path = models.CharField(max_length=255, blank=True, null=True)

    def load_config(self):
        """Parse the YAML string into a Python dictionary."""
        try:
            return yaml.safe_load(self.config_data)
        except yaml.YAMLError as e:
            return {"error": f"YAML parsing error: {e}"}

    def save_config(self, config_dict):
        """Convert a Python dictionary to YAML and save it."""
        self.config_data = yaml.dump(config_dict, default_flow_style=False)
        self.save()

    def fetch_config_from_github(self):
        """Fetch configuration from GitHub repository and update the model."""
        if not self.github_repo_url or not self.github_file_path:
            raise ValueError("GitHub repository URL or file path is not provided.")
    
        headers = {
            'Accept': 'application/vnd.github.v3.raw'
        }
        response = requests.get(f"{self.github_repo_url}/raw/branch/master/{self.github_file_path}", headers=headers)
        if response.status_code == 200:
            config_data = yaml.safe_load(response.text)
            self.save_config(config_data)
            self.data_source = VERSION_CONTROL
            self.save()
            return config_data
        else:
            raise Exception(f"Failed to fetch config from GitHub. Status code: {response.status_code}")

    def refresh(self):
        """Fetch configuration from either DB or GitHub."""
        if self.data_source == DATABASE:
            return self.load_config()
        elif self.data_source == VERSION_CONTROL:
            return self.fetch_config_from_github()
        else:
            raise ValueError("Unknown data source type.")
        
    def get_config_value(self, key, default=None):
        """Retrieve a specific value from the configuration."""
        config_dict = self.load_config()
        return config_dict.get(key, default)

    def set_config_value(self, key, value):
        """Set a specific value in the configuration and save."""
        config_dict = self.load_config()
        config_dict[key] = value
        self.save_config(config_dict)

    def __str__(self):
        return f"{self.config.name} - {self.version} ({self.environment.name})"
