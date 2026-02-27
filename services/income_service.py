from sqlalchemy import text
from config.database import engine

def add_income(user_id, source, amount, income_date, description):
    with engine.connect() as conn:
        conn.execute(text("""
            INSERT INTO income (user_id, source, amount, income_date, description)
            VALUES (:uid, :source, :amount, :date, :desc)
        """), {
            "uid": user_id,
            "source": source,
            "amount": amount,
            "date": income_date,
            "desc": description
        })
        conn.commit()

def get_income():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM income"))
        return result.fetchall()