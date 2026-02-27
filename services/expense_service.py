from sqlalchemy import text
from config.database import engine

def add_expense(user_id, category, amount, expense_date, description):
    with engine.connect() as conn:
        conn.execute(text("""
            INSERT INTO expenses (user_id, category, amount, expense_date, description)
            VALUES (:uid, :category, :amount, :date, :desc)
        """), {
            "uid": user_id,
            "category": category,
            "amount": amount,
            "date": expense_date,
            "desc": description
        })
        conn.commit()

def get_expenses():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM expenses"))
        return result.fetchall()