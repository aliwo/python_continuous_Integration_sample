from settings import base_setting


def get_settings() -> base_setting.Settings:
    """
    production, staging, local 별로 이곳에 추가하면 됩니다.
    """
    return base_setting.Settings()


settings = get_settings()
