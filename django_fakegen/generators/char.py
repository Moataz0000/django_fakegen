# Placeholder for char field generator 
from .base import BaseFieldGenerator

from django.db import models

class CharFieldGenerator(BaseFieldGenerator):

    def can_handle(self, field_type: str) -> bool:
        return field_type.get_internal_type in ('CharField', 'TextField')
    

    def generate(self, field, faker, registry) -> None:
        max_length = getattr(field, 'max_length', 50)
        return faker.text(max_nb_chars=min(max_length, 200))