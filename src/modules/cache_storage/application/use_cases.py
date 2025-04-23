from modules.cache_storage.domain.interfaces import ICacheRepository, ICacheUseCase
from config.constants import REDIS_HOST, REDIS_PORT
from modules.cache_storage.infraestructure.repository import RedisCacheService


class CacheUseCase(ICacheUseCase):
    def __init__(self, cache_repository: ICacheRepository):
        self.cache_repository = cache_repository

    def get(self, key: str) -> str | None:
        return self.cache_repository.get(key)

    def set(self, key: str, value: str, expiration_time: int):
        self.cache_repository.set(key, value, expiration_time)


class CacheUseCaseFactory:
    @staticmethod
    def create_redis_cache_use_case() -> ICacheUseCase:
        return CacheUseCase(RedisCacheService(REDIS_HOST, REDIS_PORT))
