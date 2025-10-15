import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

class Config:
    # Load database credentials from environment variables
    PGHOST = os.getenv("PGHOST")
    PGPORT = os.getenv("PGPORT")
    PGUSER = os.getenv("PGUSER")
    PGDATABASE = os.getenv("PGDATABASE")
    PGPASSWORD = os.getenv("PGPASSWORD")

    # Construct the database URI
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{PGUSER}:{PGPASSWORD}@{PGHOST}:{PGPORT}/{PGDATABASE}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # --- Flask-JWT-Extended Configuration ---
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=12)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    JWT_TOKEN_LOCATION = ["cookies"]
    JWT_COOKIE_SECURE = False
    JWT_COOKIE_SAMESITE = "Lax"
    JWT_COOKIE_CSRF_PROTECT = False
    JWT_ACCESS_COOKIE_PATH = "/"
    JWT_SESSION_COOKIE = False
