# Placeholder for many-to-many field generator 

from .base import BaseFieldGenerator

class ManyToManyFieldGenerator(BaseFieldGenerator):
    def can_handle(self, field):
        return field.get_internal_type() == "ManyToManyField"

    def generate(self, field, faker, registry):
        related_model = field.related_model
        return [registry.generate_instance(related_model, {}) for _ in range(3)]
