from db_connection import get_connection
import oracledb

def create_employee(employee_id, name, department, salary):
    connection = get_connection()
    if not connection:
        return

    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO employee (employee_id, name, department, salary)
        VALUES (:1, :2, :3, :4)
        """
        cursor.execute(query, (employee_id, name, department, salary))
        connection.commit()
        print("Employee added successfully!")
    except oracledb.DatabaseError as e:
        print(f"Error creating employee: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

