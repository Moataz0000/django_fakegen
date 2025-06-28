"""
Django-FakeGen: Intelligent Test Data Generation for Django
==========================================================

A sophisticated Django application that automatically generates realistic 
test data using advanced field introspection and intelligent faker patterns.
Perfect for populating development databases, testing, and demo environments.
"""

import os
from setuptools import setup, find_packages

# Read the contents of README file
def read_file(filename):
    """Read file contents safely"""
    try:
        with open(os.path.join(os.path.dirname(__file__), filename), encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return ""

# Get version from package
def get_version():
    """Extract version from package without importing it"""
    version = {}
    with open("django_fakegen/__init__.py") as f:
        exec(f.read(), version)
    return version.get('__version__', '3.4.4')

# Define package metadata
PACKAGE_NAME = 'django-fakegen'
AUTHOR_NAME = 'Mezo'
AUTHOR_EMAIL = 'motazfawzy73@gmail.com'
DESCRIPTION = '🎭 Intelligent test data generation for Django applications with advanced field introspection'

# Long description with emojis and formatting
LONG_DESCRIPTION = read_file("README.md") or """
# 🎭 Django-FakeGen

**Effortlessly generate realistic test data for your Django applications**

Django-FakeGen is a powerful, intelligent test data generator that understands your Django models 
and creates contextually appropriate fake data. Whether you're building prototypes, running tests, 
or populating demo databases, Django-FakeGen delivers realistic data that makes sense.

## ✨ Key Features

- 🧠 **Smart Field Detection**: Automatically recognizes field types and constraints
- 🎯 **Context-Aware Generation**: Creates data that matches your field semantics
- 🔒 **Unique Constraint Handling**: Intelligent unique field management
- 🚀 **High Performance**: Optimized for bulk data generation
- 🎨 **Extensible Architecture**: Easy to customize and extend
- 📊 **Rich Data Types**: Support for all Django field types

Transform your development workflow with intelligent test data generation!
"""

# Installation requirements with version constraints
INSTALL_REQUIRES = [
    'Django>=4.2,<6.0',
    'Faker>=20.0.0',
    'python-dateutil>=2.8.0',
]

# Optional dependencies for enhanced functionality
EXTRAS_REQUIRE = {
    'dev': [
        'pytest>=7.0.0',
        'pytest-django>=4.5.0',
        'black>=22.0.0',
        'flake8>=5.0.0',
        'mypy>=1.0.0',
    ],
    'performance': [
        'numpy>=1.21.0',
        'pandas>=1.3.0',
    ],
    'docs': [
        'sphinx>=5.0.0',
        'sphinx-rtd-theme>=1.0.0',
    ]
}

# Comprehensive classifiers for better discoverability
CLASSIFIERS = [
    # Development Status
    'Development Status :: 5 - Production/Stable',
    
    # Intended Audience
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    
    # Topic Classifications
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Software Development :: Testing',
    'Topic :: Database',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    
    # Framework
    'Framework :: Django',
    'Framework :: Django :: 4.2',
    'Framework :: Django :: 5.0',
    'Framework :: Django :: 5.1',
    
    # License
    'License :: OSI Approved :: MIT License',
    
    # Programming Language Support
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
    'Programming Language :: Python :: 3 :: Only',
    
    # Operating System
    'Operating System :: OS Independent',
    'Operating System :: POSIX',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: MacOS',
    
    # Environment
    'Environment :: Web Environment',
    'Environment :: Console',
]

# Keywords for better searchability
KEYWORDS = [
    'django', 'faker', 'test-data', 'fixtures', 'mock-data',
    'development', 'testing', 'database', 'seeding', 'generation',
    'fake-data', 'sample-data', 'demo-data', 'populate'
]

# Project URLs for enhanced package page
PROJECT_URLS = {
    'Homepage': 'https://github.com/Moataz0000/django_fakegen',
    'Documentation': 'https://github.com/Moataz0000/django_fakegen',
    'Source Code': 'https://github.com/Moataz0000/django_fakegen',
    'Bug Reports': 'https://github.com/your-username/django-fakegen/issues',
}

# Main setup configuration
setup(
    # Basic Information
    name=PACKAGE_NAME,
    version=get_version(),
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    
    # Author Information
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR_NAME,
    maintainer_email=AUTHOR_EMAIL,
    
    # URLs and Links
    url='https://github.com/your-username/django-fakegen',
    project_urls=PROJECT_URLS,
    
    # Package Discovery
    packages=find_packages(exclude=['tests*', 'docs*', 'examples*']),
    include_package_data=True,
    
    # Dependencies
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    python_requires='>=3.8',
    
    # Metadata
    classifiers=CLASSIFIERS,
    keywords=', '.join(KEYWORDS),
    license='MIT',
    
    # Entry Points (if you have management commands)
    entry_points={
        'console_scripts': [
            'django-fakegen=django_fakegen.cli:main',
        ],
    },
    
    # Package Data
    package_data={
        'django_fakegen': [
            'templates/*.html',
            'static/*',
            'locale/*/LC_MESSAGES/*',
        ],
    },
    
    # ZIP Safety
    zip_safe=False,
    
    # Platform Information
    platforms=['any'],
)