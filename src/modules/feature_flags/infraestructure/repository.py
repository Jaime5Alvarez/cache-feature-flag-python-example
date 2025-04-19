from posthog import Posthog
from src.config.constants import POSTHOG_API_KEY
from src.modules.feature_flags.domain.interfaces import IFeatureFlagRepository


class PostHogFeatureFlagRepository(IFeatureFlagRepository):
    def __init__(self):
        self.client = Posthog(api_key=POSTHOG_API_KEY)

    def is_feature_enabled(self, feature_flag_name: str, distinct_id: str) -> bool:
        feature_flag_enabled = self.client.feature_enabled(
            feature_flag_name, distinct_id
        )
        if feature_flag_enabled is None:
            return False
        return feature_flag_enabled
