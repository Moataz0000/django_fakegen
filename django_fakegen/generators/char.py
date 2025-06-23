# Placeholder for char field generator 
from ..base import BaseFieldGenerator

from django.db import models

class CharFieldGenerator(BaseFieldGenerator):

    def can_handle(self, field) -> bool:
        return field.get_internal_type() == "CharField"
    

    def generate(self, field, faker, registry) -> None:
        max_length = getattr(field, "max_length", 50)
        title = faker.sentence(nb_words=6)  
        return title[:max_length]
