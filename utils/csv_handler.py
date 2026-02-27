import pandas as pd
from utils.supabase_client import get_supabase

def upload_csv_to_table(file, table_name):
    supabase = get_supabase()

    df = pd.read_csv(file)
    rows = df.to_dict(orient="records")

    # Insert rows
    response = supabase.table(table_name).insert(rows).execute()

    return f"Uploaded {len(rows)} rows to {table_name}"
