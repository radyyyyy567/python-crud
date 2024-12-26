from db_connection import get_connection
import oracledb

def update_employee(employee_id, name=None, department=None, salary=None):
    connection = get_connection()
    if not connection:
        return

    try:
        cursor = connection.cursor()
        updates = []
        params = {}
        
        if name:
            updates.append("name = :name")
            params['name'] = name
        if department:
            updates.append("department = :department")
            params['department'] = department
        if salary:
            updates.append("salary = :salary")
            params['salary'] = salary

        if not updates:
            print("No updates provided.")
            return

        params['employee_id'] = employee_id
        query = f"""
        UPDATE employee
        SET {', '.join(updates)}
        WHERE employee_id = :employee_id
        """
        cursor.execute(query, params)
        connection.commit()
        print("Employee updated successfully!")
    except oracledb.DatabaseError as e:
        print(f"Error updating employee: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

