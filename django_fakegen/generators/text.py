# Placeholder for char field generator 
from ..base import BaseFieldGenerator

from django.db import models

class TextFieldGenerator(BaseFieldGenerator):

    def can_handle(self, field) -> bool:
        return field.get_internal_type() == "TextField"
    

    def generate(self, field, faker, registry) -> None:
        MAX_CHAR = 250
        return faker.text(max_nb_chars=250)
