# django-fakegen

A Django package for generating smart fake data for your models. It leverages [Faker](https://faker.readthedocs.io/) to automatically populate Django models with realistic data, supporting a wide range of field types, including relations.

## Features
- Generate fake data for any Django model, including related fields
- Supports bulk generation
- Customizable via field overrides
- CLI integration via Django management command

## Installation

```bash
pip install django-fakegen
```

Add `django_fakegen` to your `INSTALLED_APPS` if needed (not strictly required for management command usage).

## Usage

### Command Line

Generate 10 fake instances for a model:

```bash
python manage.py fakegen app_label.ModelName
```

Generate a custom number of instances:

```bash
python manage.py fakegen app_label.ModelName --count 50
```

### Programmatic Usage

You can use the registry directly in your code:

```python
from django_fakegen.registry import registry

# Generate a single instance
instance = registry.generate_instance(MyModel)

# Generate multiple instances
instances = registry.bulk_generate('app_label.ModelName', count=20)
```

## Supported Fields

django-fakegen supports the following Django field types:

| Field Type           | Generator Behavior                                  |
|---------------------|-----------------------------------------------------|
| CharField           | Title-like string, respects `max_length`             |
| TextField           | Realistic text, up to 250 chars                     |
| IntegerField        | Random integer (0-100)                              |
| PositiveIntegerField| Random integer (0-100)                              |
| FloatField          | Random float (5 digits left, 2 right)               |
| BooleanField        | Random boolean                                      |
| DateTimeField       | Random datetime (this year)                         |
| DateField           | Random date (this year)                             |
| TimeField           | Random time                                         |
| EmailField          | Random email address                                |
| ForeignKey          | Random related instance                             |
| OneToOneField       | Random related instance                             |
| ManyToManyField     | List of 3 random related instances                  |

## Example

Suppose you have a model:

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    published = models.BooleanField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

You can generate fake data for `Book` (and related `Author`) with:

```bash
python manage.py fakegen myapp.Book --count 5
```

Or programmatically:

```python
from django_fakegen.registry import registry
books = registry.bulk_generate('myapp.Book', count=5)
```

## Extending

You can add your own field generators by subclassing `BaseFieldGenerator` and adding them to the registry.

## License

MIT 