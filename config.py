import os


class Config:
    DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///foo.db")
    DATA_DIRECTORY = os.environ.get("DATA_DIRECTORY", "data")


class TestConfig(Config):
    DATABASE_URL = os.environ.get("TEST_DATABASE_URL", "sqlite:///tests/test_foo.db")
