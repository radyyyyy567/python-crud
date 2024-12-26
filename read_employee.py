from db_connection import get_connection
import oracledb

def read_employees():
    connection = get_connection()
    if not connection:
        return

    try:
        cursor = connection.cursor()
        query = "SELECT * FROM employee"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except oracledb.DatabaseError as e:
        print(f"Error reading employees: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

read_employees()