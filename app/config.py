import os   # импортируем библиотеку OS чтобы получить доступ операционной системой
from dotenv import load_dotenv

load_dotenv()  # функция загружает переменные из env файла в операционную систему


DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_USER = os.getenv("DB_USER", "")
DB_NAME = os.getenv("DB_NAME", "")
DB_HOST = os.getenv("DB_HOST", "")
DB_PORT = os.getenv("DB_PORT", 0)
DB_SERVER = os.getenv("DB_SERVER")

SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}"
