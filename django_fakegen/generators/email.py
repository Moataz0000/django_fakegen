# Placeholder for email field generator 

from ..base import BaseFieldGenerator
from django.db import models
from ..base import BaseFieldGenerator
import uuid


class EmailFieldGenerator(BaseFieldGenerator):
    def can_handle(self, field):
        return isinstance(field, models.EmailField)

    def generate(self, field, faker, registry):
        if getattr(field, 'unique', False):
            return self._generate_unique_email(field, faker, registry)
        else:
            return faker.email()
    
    def _generate_unique_email(self, field, faker, registry):
        """Generate a unique email for fields with unique=True"""
        model_class = field.model
        field_name = field.name
        
        max_attempts = 10
        for _ in range(max_attempts):
            email = faker.email()
            if not self._email_exists(model_class, field_name, email):
                return email
        
        return self._generate_uuid_email(model_class, field_name, faker)
    
    def _email_exists(self, model_class, field_name, email):
        """Check if email already exists in database"""
        try:
            filter_kwargs = {field_name: email}
            return model_class.objects.filter(**filter_kwargs).exists()
        except Exception:
            return True
    
    def _generate_uuid_email(self, model_class, field_name, faker):
        """Generate a unique email using UUID"""
        base_domains = ['example.com', 'test.com', 'demo.com']
        domain = faker.random_element(base_domains)
        
        # Keep generating until we find a unique one
        while True:
            unique_id = uuid.uuid4().hex[:8]
            email = f"user_{unique_id}@{domain}"
            
            if not self._email_exists(model_class, field_name, email):
                return email