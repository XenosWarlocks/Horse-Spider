import sqlite3
import pandas as pd

def store_data_to_db(csv_file, db_file):
    conn = sqlite3.connect(db_file)
    df = pd.read_csv(csv_file)
    df.to_sql('esg_data', conn, if_exists='replace', index=False)
    conn.close()
