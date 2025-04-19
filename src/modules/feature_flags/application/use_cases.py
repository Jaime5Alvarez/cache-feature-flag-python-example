from src.config.constants import REDIS_HOST, REDIS_PORT
from src.modules.feature_flags.domain.interfaces import (
    IFeatureFlagRepository,
    IFeatureFlagUseCase,
)
from src.modules.feature_flags.infraestructure.repository import (
    PostHogFeatureFlagRepository,
)
import redis


class CachedFeatureFlagUseCase(IFeatureFlagUseCase):
    def __init__(self, feature_flag_use_case: IFeatureFlagUseCase):
        self.feature_flag_use_case = feature_flag_use_case
        self.cache = redis.Redis(
            host=REDIS_HOST, port=REDIS_PORT, decode_responses=True
        )

    def is_feature_enabled(self, feature_flag_name: str, distinct_id: str) -> bool:
        cache_key = f"feature_flags:{distinct_id}:{feature_flag_name}"
        cached_value = self.cache.get(cache_key)

        if cached_value:
            print(f"Cache hit for {cache_key}")
            return cached_value == "true"

        feature_flag_enabled = self.feature_flag_use_case.is_feature_enabled(
            feature_flag_name, distinct_id
        )
        self.cache.set(cache_key, "true" if feature_flag_enabled else "false")
        return feature_flag_enabled


class CachedFeatureFlagUseCaseFactory:
    @staticmethod
    def create_posthog() -> IFeatureFlagUseCase:
        return CachedFeatureFlagUseCase(
            FeatureFlagUseCase(PostHogFeatureFlagRepository())
        )


class FeatureFlagUseCase(IFeatureFlagUseCase):
    def __init__(self, feature_flag_repository: IFeatureFlagRepository):
        self.feature_flag_repository = feature_flag_repository

    def is_feature_enabled(self, feature_flag_name: str, distinct_id: str) -> bool:
        return self.feature_flag_repository.is_feature_enabled(
            feature_flag_name, distinct_id
        )


class FeatureFlagUseCaseFactory:
    @staticmethod
    def create_posthog() -> IFeatureFlagUseCase:
        return FeatureFlagUseCase(PostHogFeatureFlagRepository())
