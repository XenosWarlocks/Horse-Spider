import sqlite3
import pandas as pd

from database.db_config import DatabaseConfig

def store_data_to_db(csv_file, db_config):
    # Extract the database file path
    db_file = db_config.db_file if isinstance(db_config, DatabaseConfig) else db_config

    try:
        conn = sqlite3.connect(db_file)
        df = pd.read_csv(csv_file)

        df.to_sql('esg_data', conn, if_exists='append', index=False)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()
