# Placeholder for char field generator 
from .base import BaseFieldGenerator

from django.db import models

class CharFieldGenerator(BaseFieldGenerator):

    def can_handle(self, field) -> bool:
        return field.get_internal_type() in ("CharField", "TextField")
    

    def generate(self, field, faker, registry) -> None:
        max_length = getattr(field, "max_length", 50)
        limit = max_length if isinstance(max_length, int) and max_length < 200 else 200
        return faker.text(max_nb_chars=limit)
