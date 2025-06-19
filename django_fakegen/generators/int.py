# Placeholder for int field generator 
from .base import BaseFieldGenerator

class IntFieldGenerator(BaseFieldGenerator):
    def can_handle(self, field):
        return field.get_internal_type() in ("IntegerField", "PositiveIntegerField")

    def generate(self, field, faker, registry):
        return faker.random_int(min=0, max=100)
