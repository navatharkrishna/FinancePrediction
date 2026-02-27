def upload_csv_to_table(file, table_name):
    df = pd.read_csv(file)

    # Use engine from config
    from config.database import engine

    df.to_sql(
        table_name,
        engine,
        if_exists="append",
        index=False,
        method="multi"
    )
