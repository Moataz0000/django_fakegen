# Placeholder for datetime field generator 
from .base import BaseFieldGenerator

class DateTimeFieldGenerator(BaseFieldGenerator):
    def can_handle(self, field):
        return field.get_internal_type() == "DateTimeField"

    def generate(self, field, faker, registry):
        return faker.date_time_this_year()
