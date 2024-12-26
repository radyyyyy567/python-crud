from db_connection import get_connection
import oracledb

def read_employee_by_id(employee_id):
    connection = get_connection()
    if not connection:
        return

    try:
        cursor = connection.cursor()
        query = "SELECT * FROM employee WHERE id= :employee_id"
        cursor.execute(query, {'employee_id': employee_id})
        row = cursor.fetchall()
        return row
    except oracledb.DatabaseError as e:
        print(f"Error reading employees: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

