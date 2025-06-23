# Placeholder for email field generator 

from ..base import BaseFieldGenerator

class EmailFieldGenerator(BaseFieldGenerator):
    def can_handle(self, field):
        return field.get_internal_type() == "EmailField"

    def generate(self, field, faker, registry):
        return faker.email()
