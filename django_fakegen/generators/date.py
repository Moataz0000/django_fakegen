# Placeholder for date field generator 
from ..base import BaseFieldGenerator

class DateFieldGenerator(BaseFieldGenerator):
    def can_handle(self, field):
        return field.get_internal_type() == "DateField"

    def generate(self, field, faker, registry):
        return faker.date_this_year()
