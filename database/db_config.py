import sqlite3
from sqlite3 import Error
import os
from contextlib import contextmanager

class DatabaseConfig:
    def __init__(self, db_file='esg_data.db'):
        self.db_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), db_file)
        self._ensure_database_exists()

    def _ensure_database_exists(self):
        """Ensure the database file exists; if not, create the tables."""
        if not os.path.exists(self.db_file):
            self._create_tables()

    def _create_tables(self):
        """Create necessary tables if they do not exist."""
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS esg_data (
                        id INTEGER PRIMARY KEY,
                        title TEXT NOT NULL,
                        url TEXT NOT NULL UNIQUE,
                        content TEXT NOT NULL
                    );
                ''')
                conn.commit()
        except Error as e:
            print(f"Error creating tables: {e}")
            raise

    @contextmanager
    def _get_connection(self):
        """Context manager to handle database connections."""
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
            yield conn
        except Error as e:
            print(f"Database connection error: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def insert_esg_data(self, title, url, content):
        """Insert data into the esg_data table."""
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO esg_data (title, url, content)
                    VALUES (?, ?, ?)
                ''', (title, url, content))
                conn.commit()
        except sqlite3.IntegrityError as e:
            print(f"Data already exists for URL {url}: {e}")
        except Error as e:
            print(f"Error inserting data: {e}")
            raise

    def fetch_all_data(self):
        """Fetch all data from the esg_data table."""
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM esg_data')
                rows = cursor.fetchall()
                return rows
        except Error as e:
            print(f"Error fetching data: {e}")
            raise

    def delete_data_by_id(self, data_id):
        """Delete a specific entry from the esg_data table by ID."""
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM esg_data WHERE id = ?', (data_id,))
                conn.commit()
        except Error as e:
            print(f"Error deleting data: {e}")
            raise

    def update_data(self, data_id, title=None, url=None, content=None):
        """Update an entry in the esg_data table by ID."""
        fields = []
        values = []
        if title:
            fields.append("title = ?")
            values.append(title)
        if url:
            fields.append("url = ?")
            values.append(url)
        if content:
            fields.append("content = ?")
            values.append(content)
        
        if not fields:
            print("No fields to update")
            return

        values.append(data_id)
        query = f"UPDATE esg_data SET {', '.join(fields)} WHERE id = ?"
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(query, values)
                conn.commit()
        except Error as e:
            print(f"Error updating data: {e}")
            raise

# Testing the code
# if __name__ == "__main__":
#     # Example usage
#     db_config = DatabaseConfig()

#     # Insert data
#     db_config.insert_esg_data(
#         title="ESG Risk in Bank Investment",
#         url="https://example.com/article1",
#         content="This article discusses ESG risks in banking."
#     )

#     # Fetch all data
#     all_data = db_config.fetch_all_data()
#     print(all_data)

#     # Update data
#     db_config.update_data(1, content="Updated content")

#     # Delete data by ID
#     db_config.delete_data_by_id(1)
