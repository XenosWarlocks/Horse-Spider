import sqlite3

def create_db(db_file):
    conn = sqlite3.connect(db_file)
    # Create tables if necessary
    conn.execute('''CREATE TABLE IF NOT EXISTS esg_data
                    (title TEXT, url TEXT, content TEXT)''')
    conn.close()
