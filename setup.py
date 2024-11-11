from setuptools import setup, find_packages

setup(
    name='django_cloud_config',
    version='0.0.1.beta',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django>=3.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Django',
    ],
)
