from src.modules.feature_flags.domain.interfaces import (
    IFeatureFlagRepository,
    IFeatureFlagUseCase,
)
from src.modules.feature_flags.infraestructure.repository import (
    PostHogFeatureFlagRepository,
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
    def create_feature_flag_use_case() -> IFeatureFlagUseCase:
        return FeatureFlagUseCase(PostHogFeatureFlagRepository())
