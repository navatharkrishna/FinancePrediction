import pandas as pd
from utils.supabase_client import get_supabase

def upload_csv_to_table(file, table_name):
    supabase = get_supabase()

    # Read CSV
    df = pd.read_csv(file)

    # Convert to list of dicts (column names must match table)
    rows = df.to_dict(orient="records")

    # Insert into Supabase table
    response = supabase.table(table_name).insert(rows).execute()

    return f"Uploaded {len(rows)} rows to {table_name}"
