# Placeholder for email field generator 

from ..base import BaseFieldGenerator
from faker import Faker
from django.db import models

class EmailFieldGenerator(BaseFieldGenerator):
    def can_handle(self, field):
        return isinstance(field, models.EmailField)

    def generate(self, field, faker, registry):
        return faker.email()
