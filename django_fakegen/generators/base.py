from abc import ABC, abstractmethod


class BaseFieldGenerator(ABC):
    
    @abstractmethod
    def can_handle(self, field_type: str) -> None:
        pass

    @abstractmethod
    def generate(self, field: str, faker, registry) -> None:
        pass