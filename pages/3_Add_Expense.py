import streamlit as st
from services.expense_service import add_expense

st.title("➖ Add Expense")

user_id = st.text_input("User ID")
category = st.text_input("Category")
amount = st.number_input("Amount", min_value=0.0)
date = st.date_input("Date")
description = st.text_area("Description")

if st.button("Add Expense"):
    add_expense(user_id, category, amount, date, description)
    st.success("Expense Added Successfully!")