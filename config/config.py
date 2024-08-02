import os


class Config:
    SECRET_KEY = 'projectsecretkey'
    ENCRYPTION_KEY = b'KJwPYB0LjXOabX6Sk0p2Sfsw6N6SC9Zf3ziKoZJtnu8='
    SERVER_ADDRESS = 'localhost'
    SERVER_PORT = 8000
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATABASE_URI = os.path.join(BASE_DIR, '../database/iot_framework.db')


config = Config()
