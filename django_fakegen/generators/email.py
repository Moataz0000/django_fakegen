# Placeholder for email field generator 

from ..base import BaseFieldGenerator
from faker import Faker
from django.db.models import EmailField

class EmailFieldGenerator(BaseFieldGenerator):
    def can_handle(self, field):
        return isinstance(field, EmailField)

    def generate(self, field, faker: Faker, registry):
        return faker.email()
