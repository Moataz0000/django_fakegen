# Placeholder for one-to-one field generator 

from ..base import BaseFieldGenerator

class OneToOneFieldGenerator(BaseFieldGenerator):
    def can_handle(self, field):
        return field.get_internal_type() == "OneToOneField"

    def generate(self, field, faker, registry):
        return registry.generate_instance(field.related_model, {})
