# Placeholder for boolean field generator 

from ..base import BaseFieldGenerator

class BooleanFieldGenerator(BaseFieldGenerator):
    def can_handle(self, field):
        return field.get_internal_type() == "BooleanField"

    def generate(self, field, faker, registry):
        return faker.boolean()
