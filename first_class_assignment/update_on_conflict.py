import json
import psycopg2
from database_connect_class import DatabaseConnect

query = """
            CREATE TABLE student_info(
                std_id serial PRIMARY KEY,
                std_name VARCHAR UNIQUE,
                email VARCHAR NOT NULL,
                active bool NOT NULL DEFAULT TRUE
            )
    """

db_obj = DatabaseConnect()
conn = None

try:
    # Initialize connection object
    conn = db_obj.db_connect()
    # Commit for database changes and store changes
    conn.autocommit = True
    # Create cursor to perform SQL queries on connected database
    cursor = conn.cursor()
    query = """
                INSERT INTO 
                    student_info(std_name, email)
                VALUES(
                    'Imran Khan',
                    'duetboyimran@gmail.com'
                )
                ON CONFLICT (std_name) DO UPDATE 
                SET email='khalekuzzamanimran@gmail.com'
    """
    
    # Execute query by cursor on connected database
    cursor.execute(query)

    print("Data is Updated into Data Info..")

except (Exception, psycopg2.DatabaseError) as error:
        print(error)

finally:
    if conn:
        conn.close()
        cursor.close()


