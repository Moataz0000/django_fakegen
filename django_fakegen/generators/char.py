# Placeholder for char field generator 
from ..base import BaseFieldGenerator

from django.db import models

class CharFieldGenerator(BaseFieldGenerator):

    def can_handle(self, field) -> bool:
        # Check if it's a CharField but NOT an EmailField or URLField
        return (isinstance(field, models.CharField) and 
                not isinstance(field, models.EmailField) and
                not isinstance(field, (models.URLField, models.SlugField)))
    
    def generate(self, field, faker, registry):
        max_length = getattr(field, "max_length", 50)
        title = faker.sentence(nb_words=6)  
        return title[:max_length]
