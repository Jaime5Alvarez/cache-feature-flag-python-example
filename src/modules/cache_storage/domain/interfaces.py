from abc import ABC, abstractmethod
from typing import Optional


class ICacheRepository(ABC):
    @abstractmethod
    def get(self, key: str) -> str | None:
        pass

    @abstractmethod
    def set(self, key: str, value: str, expiration_time: int):
        pass


class ICacheUseCase(ABC):
    @abstractmethod
    def get(self, key: str) -> str | None:
        pass

    @abstractmethod
    def set(self, key: str, value: str, expiration_time: int):
        pass
