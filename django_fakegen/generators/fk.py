# Placeholder for foreign key field generator


from .base import BaseFieldGenerator

class ForeignKeyGenerator(BaseFieldGenerator):
    def can_handle(self, field):
        return field.get_internal_type() == "ForeignKey"

    def generate(self, field, faker, registry):
        inst = registry.generate_instance(field.related_model, {})
        return inst
