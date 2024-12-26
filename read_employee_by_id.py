from db_connection import get_connection
import oracledb

def read_employee_by_id(employee_id):
    connection = get_connection()
    if not connection:
        return
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM employee WHERE employee_id = :employee_id"
        cursor.execute(query, {'employee_id': employee_id})
        raws = cursor.fetchall()
        raw = raws[0]
        row = [str(raw[0]), raw[1], raw[2], raw[3]]
        return row
    except oracledb.DatabaseError as e:
        print(f"Error reading employees: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

