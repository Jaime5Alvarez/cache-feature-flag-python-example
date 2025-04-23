from modules.cache_storage.domain.interfaces import ICacheRepository
import redis


class RedisCacheService(ICacheRepository):
    def __init__(self, host: str, port: int):
        self.cache = redis.Redis(host=host, port=port, decode_responses=True)

    def get(self, key: str) -> str | None:
        value = self.cache.get(key)
        if value is None:
            return None
        return str(value)

    def set(self, key: str, value: str, expiration_time: int):
        self.cache.set(key, value, ex=expiration_time)
