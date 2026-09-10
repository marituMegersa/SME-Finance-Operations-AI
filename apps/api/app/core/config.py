import os

class Settings:
    PROJECT_NAME: str = "SME Finance & Cash Flow Operations API"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://copilot_user:copilot_secure_password@localhost:5432/finance_operations_db")

settings = Settings()
