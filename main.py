from src.modules.feature_flags.application.use_cases import FeatureFlagUseCaseFactory
from src.modules.feature_flags.domain.enums import FeatureFlagName
from src.config.mock_users import MockUsers


def main():
    print("Hello from cache-feature-flag-python-example!")
    feature_flag_use_case = FeatureFlagUseCaseFactory.create_posthog()
    if feature_flag_use_case.is_feature_enabled(
        FeatureFlagName.ADMIN_ACCESS.value, MockUsers.USER_5.value
    ):
        print("Feature flag is enabled")
    else:
        print("Feature flag is disabled")
    


if __name__ == "__main__":
    main()
