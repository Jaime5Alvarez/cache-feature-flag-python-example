from modules.feature_flags.application.use_cases import (
    CachedFeatureFlagUseCaseFactory,
)
from modules.feature_flags.domain.enums import FeatureFlagName
from config.mock_users import MockUsers
from timeit import timeit


def main():
    feature_flag_use_case = CachedFeatureFlagUseCaseFactory.create_posthog()
    if feature_flag_use_case.is_feature_enabled(
        FeatureFlagName.ADMIN_ACCESS.value, MockUsers.USER_4.value
    ):
        print("Feature flag is enabled")
    else:
        print("Feature flag is disabled")


if __name__ == "__main__":
    tiempo = timeit(lambda: main(), number=1)
    print(f"Tiempo de ejecución: {tiempo:.4f} segundos") 