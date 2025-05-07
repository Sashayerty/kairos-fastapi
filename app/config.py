class Config:
    # Список моделей: https://docs.mistral.ai/getting-started/models/models_overview/
    MISTRAL_DEFAULT_MODEL: str = "mistral-large-latest"
    # Путь к БД
    DATABASE_PATH: str = "./database/kairos.db"


config = Config()
