from abc import ABC, abstractmethod


class BaseFieldGenerator:
    def can_handle(self, field) -> bool:
        """
        Return True if this generator knows how to generate data
        for the given Django field.
        """
        raise NotImplementedError

    def generate(self, field, faker, registry):
        """
        Return a single fake value for this field.
        """
        raise NotImplementedError