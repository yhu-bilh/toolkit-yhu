# SQL Server Connection and Query Examples

# Method 1: Using pyodbc (recommended)
import pyodbc
import os
import pandas as pd

def connect_sqlserver_pyodbc():
    # Connection string components
    server = 'your_server_name'  # e.g., 'localhost' or 'server.domain.com'
    database = 'your_database_name'
    username = 'your_username'
    password = 'your_password'

    # Connection string
    conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

    try:
        # Establish connection
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Example query
        query = "SELECT TOP 10 * FROM your_table_name"
        cursor.execute(query)

        # Fetch results
        results = cursor.fetchall()
        for row in results:
            print(row)

        # Close connection
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error: {e}")

def check_file_exists_and_size(file_path):
    """Check if file exists and get its size"""
    if os.path.exists(file_path):
        if os.path.isfile(file_path):
            size = os.path.getsize(file_path)
            print(f"File exists: {file_path}")
            print(f"Size: {size} bytes ({format_file_size(size)})")
            return size
        else:
            print(f"Path exists but is not a file: {file_path}")
            return None
    else:
        print(f"File does not exist: {file_path}")
        return None

def format_file_size(size_bytes):
    """Convert bytes to human-readable format"""
    if size_bytes == 0:
        return "0 B"

    size_names = ["B", "KB", "MB", "GB", "TB"]
    import math
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_names[i]}"

# Main execution
if __name__ == "__main__":
    # Choose your preferred method
    connect_sqlserver_pyodbc()
    # connect_sqlserver_sqlalchemy()
    # connect_windows_auth()
    # parameterized_query()
    # modify_data()