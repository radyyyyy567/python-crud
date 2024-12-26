import oracledb

def get_connection():
    try:
        connection = oracledb.connect(
            user="sys",
            password="admin",
            dsn="localhost:1521/free",
            mode=oracledb.SYSDBA
        )
        print("work")
        return connection
    except oracledb.DatabaseError as e:
        print("not work")
        print(f"Error connecting to Oracle: {e}")
        return None
    
get_connection()