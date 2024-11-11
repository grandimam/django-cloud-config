from setuptools import setup, find_packages

setup(
    name="django_cloud_config",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django>=3.2",
        "redis>=3.5.3",
    ],
)
