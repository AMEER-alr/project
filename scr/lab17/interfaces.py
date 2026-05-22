from abc import ABC, abstractmethod
from typing import Any


class Printable(ABC):

    @abstractmethod
    def to_string(self) -> str:
        pass


class Comparable(ABC):

    @abstractmethod
    def compare_to(self, other: Any) -> int:
        pass


class MedicalInfo(ABC):

    @abstractmethod
    def get_medical_summary(self) -> str:
        pass