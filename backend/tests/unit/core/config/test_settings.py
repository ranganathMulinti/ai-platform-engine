from core.config import Environment, Settings


def test_settings_initialization():
    settings = Settings()
    assert settings.app_name == "AI Platform Engine"
    assert settings.app_version == "0.1.0"
    assert settings.environment == Environment.development
    assert settings.debug is True
    assert settings.host == "0.0.0.0"
    assert settings.port == 8000
    assert settings.database_url == "sqlite:///./test.db"
    assert settings.redis_url == "redis://localhost:6379"
    assert settings.secret_key
