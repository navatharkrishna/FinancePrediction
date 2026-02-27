import pandas as pd
from config.database import engine

def upload_csv_to_table(file, table_name):
    df = pd.read_csv(file)

    df.to_sql(
        table_name,
        engine,
        if_exists="append",
        index=False,
        method="multi"
    )

    return f"Uploaded {len(df)} rows to {table_name}"
