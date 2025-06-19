# Placeholder for time field generator 
from .base import BaseFieldGenerator

class TimeFieldGenerator(BaseFieldGenerator):
    def can_handle(self, field):
        return field.get_internal_type() == "TimeField"

    def generate(self, field, faker, registry):
        return faker.time()
