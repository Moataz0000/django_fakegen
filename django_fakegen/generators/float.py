# Placeholder for float field generator 
from .base import BaseFieldGenerator

class FloatFieldGenerator(BaseFieldGenerator):
    def can_handle(self, field):
        return field.get_internal_type() == "FloatField"

    def generate(self, field, faker, registry):
        return faker.pyfloat(left_digits=5, right_digits=2)
