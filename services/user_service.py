from sqlalchemy import text
from config.database import engine

def create_user(full_name, email, password_hash):
    with engine.connect() as conn:
        conn.execute(text("""
            INSERT INTO users (full_name, email, password_hash)
            VALUES (:name, :email, :password)
        """), {
            "name": full_name,
            "email": email,
            "password": password_hash
        })
        conn.commit()

def get_users():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM users"))
        return result.fetchall()