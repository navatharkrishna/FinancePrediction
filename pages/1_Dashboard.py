import streamlit as st
import pandas as pd
from services.income_service import get_income
from services.expense_service import get_expenses

st.title("📊 Dashboard")

income = get_income()
expenses = get_expenses()

income_df = pd.DataFrame(income)
expense_df = pd.DataFrame(expenses)

st.subheader("Income")
st.dataframe(income_df)

st.subheader("Expenses")
st.dataframe(expense_df)

if not income_df.empty:
    st.metric("Total Income", income_df["amount"].sum())

if not expense_df.empty:
    st.metric("Total Expenses", expense_df["amount"].sum())