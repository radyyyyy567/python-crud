from db_connection import get_connection
import oracledb

def delete_employee(employee_id):
    connection = get_connection()
    if not connection:
        return

    try:
        cursor = connection.cursor()
        query = "DELETE FROM employee WHERE employee_id = :employee_id"
        cursor.execute(query, {'employee_id': employee_id})
        connection.commit()
        print("Employee deleted successfully!")
    except oracledb.DatabaseError as e:
        print(f"Error deleting employee: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
