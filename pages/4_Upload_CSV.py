import streamlit as st
from utils.csv_handler import upload_csv_to_table

st.title("📂 Upload CSV")

file = st.file_uploader("Upload CSV File", type=["csv"])
table_name = st.text_input("Enter Table Name")

if st.button("Upload"):
    if file and table_name:
        upload_csv_to_table(file, table_name)
        st.success("File Uploaded Successfully!")