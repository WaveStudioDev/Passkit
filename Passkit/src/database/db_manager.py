import sqlite3
from sqlite3 import Error

class DatabaseManager:
    def __init__(self, db_file):
        self.db_file = db_file
        """Initialize the database manager with a database file."""
        self.connection = self.create_connection(db_file)
        self.create_table()

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(e)
        return conn

    def create_table(self):
        """Create a table if it doesn't exist."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            value TEXT NOT NULL
        );
        """
        self.execute_query(create_table_sql)

    def execute_query(self, query, params=()):
        """Execute a single query."""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(e)

    def create_record(self, name, value):
        """Create a new record in the database."""
        query = "INSERT INTO records (name, value) VALUES (?, ?);"
        self.execute_query(query, (name, value))

    def read_records(self):
        """Query all records from the database."""
        query = "SELECT * FROM records;"
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def update_record(self, record_id, name, value):
        """Update a record in the database."""
        query = "UPDATE records SET name = ?, value = ? WHERE id = ?;"
        self.execute_query(query, (name, value, record_id))

    def delete_record(self, record_id):
        """Delete a record from the database."""
        query = "DELETE FROM records WHERE id = ?;"
        self.execute_query(query, (record_id,))

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed")

def get_session(db_file):
    """Function to get a new database session."""
    return DatabaseManager(db_file)