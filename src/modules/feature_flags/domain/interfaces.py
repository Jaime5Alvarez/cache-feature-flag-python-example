from abc import ABC, abstractmethod


class IFeatureFlagUseCase(ABC):
    @abstractmethod
    def is_feature_enabled(self, feature_flag_name: str, distinct_id: str) -> bool:
        pass


class IFeatureFlagRepository(ABC):
    @abstractmethod
    def is_feature_enabled(self, feature_flag_name: str, distinct_id: str) -> bool:
        pass
