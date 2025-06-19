# Placeholder for registry logic 
from faker import Faker
from django.apps import apps

from django_fakegen.generators.char import CharFieldGenerator
from django_fakegen.generators.int import IntFieldGenerator
from django_fakegen.generators.float import FloatFieldGenerator
from django_fakegen.generators.boolean import BooleanFieldGenerator
from django_fakegen.generators.datetime import DateTimeFieldGenerator
from django_fakegen.generators.date import DateFieldGenerator
from django_fakegen.generators.time import TimeFieldGenerator
from django_fakegen.generators.email import EmailFieldGenerator
from django_fakegen.generators.fk import ForeignKeyGenerator
from django_fakegen.generators.o2o import OneToOneFieldGenerator
from django_fakegen.generators.m2m import ManyToManyFieldGenerator
from django_fakegen.generators.text import TextFieldGenerator



class GeneratorRegistry:
    def __init__(self):
        self.faker = Faker()
        self.generators = [
            CharFieldGenerator(),
            TextFieldGenerator(),
            IntFieldGenerator(),
            FloatFieldGenerator(),
            BooleanFieldGenerator(),
            DateTimeFieldGenerator(),
            DateFieldGenerator(),
            TimeFieldGenerator(),
            EmailFieldGenerator(),
            ForeignKeyGenerator(),
            OneToOneFieldGenerator(),
            ManyToManyFieldGenerator(),
        ]

    def get_model(self, label):
        return apps.get_model(label)


    def generate_instance(self, model, overrides=None):
        data = {}
        m2m_data = []
        for field in model._meta.get_fields():
            if not getattr(field, 'editable', False) or field.auto_created:
                continue
            name = field.name
            if overrides and name in overrides:
                data[name] = overrides[name]
                continue
            for gen in self.generators:
                if gen.can_handle(field):
                    val = gen.generate(field, self.faker, self)
                    if field.many_to_many:
                        m2m_data.append((name, val))
                    else:
                        data[name] = val
                    break
        instance = model(**data)
        instance.save()
        for name, val in m2m_data:
            getattr(instance, name).set(val)
        return instance

    
    def bulk_generate(self, label, count, overrides=None):
        model = self.get_model(label)
        return [self.generate_instance(model, overrides) for _ in range(count)]

registry = GeneratorRegistry()
