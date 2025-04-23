from config.constants import REDIS_HOST, REDIS_PORT
from modules.feature_flags.domain.interfaces import IFeatureFlagUseCase
import redis


class CachedFeatureFlagUseCase(IFeatureFlagUseCase):
    def __init__(
        self, feature_flag_use_case: IFeatureFlagUseCase, expiration_time: int = 3600
    ):
        self.feature_flag_use_case = feature_flag_use_case
        self.cache = redis.Redis(
            host=REDIS_HOST, port=REDIS_PORT, decode_responses=True
        )
        self.expiration_time = expiration_time

    def is_feature_enabled(self, feature_flag_name: str, distinct_id: str) -> bool:
        cache_key = f"feature_flags:{feature_flag_name}:{distinct_id}"
        cached_value = self.cache.get(cache_key)

        if cached_value:
            print(f"Cache hit for {cache_key}")
            return cached_value == "true"

        feature_flag_enabled = self.feature_flag_use_case.is_feature_enabled(
            feature_flag_name, distinct_id
        )
        self.cache.set(
            cache_key, "true" if feature_flag_enabled else "false", ex=self.expiration_time
        )
        return feature_flag_enabled 