import streamlit as st
from services.income_service import add_income

st.title("➕ Add Income")

user_id = st.text_input("User ID")
source = st.text_input("Source")
amount = st.number_input("Amount", min_value=0.0)
date = st.date_input("Date")
description = st.text_area("Description")

if st.button("Add Income"):
    add_income(user_id, source, amount, date, description)
    st.success("Income Added Successfully!")