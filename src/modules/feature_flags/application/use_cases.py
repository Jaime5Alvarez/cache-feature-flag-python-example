from modules.feature_flags.domain.interfaces import (
    IFeatureFlagRepository,
    IFeatureFlagUseCase,
)
from modules.feature_flags.infraestructure.repository import (
    PostHogFeatureFlagRepository,
)


from modules.cache_storage.domain.interfaces import ICacheUseCase
from modules.cache_storage.application.use_cases import CacheUseCaseFactory


class CachedFeatureFlagUseCase(IFeatureFlagUseCase):
    def __init__(
        self,
        feature_flag_use_case: IFeatureFlagUseCase,
        cache_repository: ICacheUseCase,
        expiration_time: int = 3600,
    ):
        self.feature_flag_use_case = feature_flag_use_case
        self.cache = cache_repository
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
            cache_key, "true" if feature_flag_enabled else "false", self.expiration_time
        )
        return feature_flag_enabled


class FeatureFlagUseCase(IFeatureFlagUseCase):
    def __init__(self, feature_flag_repository: IFeatureFlagRepository):
        self.feature_flag_repository = feature_flag_repository

    def is_feature_enabled(self, feature_flag_name: str, distinct_id: str) -> bool:
        return self.feature_flag_repository.is_feature_enabled(
            feature_flag_name, distinct_id
        )


class CachedFeatureFlagUseCaseFactory:
    @staticmethod
    def create_posthog() -> IFeatureFlagUseCase:
        return CachedFeatureFlagUseCase(
            FeatureFlagUseCase(PostHogFeatureFlagRepository()),
            CacheUseCaseFactory.create_redis_cache_use_case(),
        )


class FeatureFlagUseCaseFactory:
    @staticmethod
    def create_posthog() -> IFeatureFlagUseCase:
        return FeatureFlagUseCase(PostHogFeatureFlagRepository())
