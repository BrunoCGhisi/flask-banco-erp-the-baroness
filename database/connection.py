import psycopg2

from psycopg2.extras import RealDictCursor

from config import Config

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "baronesHotel",
    "user": "postgres",
    "password": "1234"
}

def get_connection():
    return psycopg2.connect(
        host=Config.DB_HOST,
        port=Config.DB_PORT,
        database=Config.DB_NAME,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        cursor_factory=RealDictCursor
    )