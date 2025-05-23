from posthog import Posthog
from config.constants import POSTHOG_API_KEY
from modules.feature_flags.domain.interfaces import IFeatureFlagRepository


class PostHogFeatureFlagRepository(IFeatureFlagRepository):
    def __init__(self):
        self.client = Posthog(POSTHOG_API_KEY, host="https://eu.i.posthog.com")

    def is_feature_enabled(self, feature_flag_name: str, distinct_id: str) -> bool:
        print(
            f"Checking feature flag {feature_flag_name} for distinct_id {distinct_id}"
        )
        feature_flag_enabled = self.client.feature_enabled(
            feature_flag_name, distinct_id
        )
        if feature_flag_enabled is None:
            return False
        return feature_flag_enabled
