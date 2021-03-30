import json
import psycopg2
from psycopg2 import extras
from database_connect_class import DatabaseConnect

with open('data/data.json') as file_obj:
    json_data = json.load(file_obj)


query = """
            INSERT INTO 
                data_info
            VALUES(
                %(uuid)s,
                %(data)s,
                %(min)s,
                %(max)s,
                %(avg)s
            )
            ON CONFLICT DO NOTHING
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
    
    # Execute query by cursor on connected database
    psycopg2.extras.execute_batch(cursor, query, json_data)
    print("Data is inserted into Data Info..")

except (Exception, psycopg2.DatabaseError) as error:
        print(error)

finally:
    if conn:
        conn.close()
        cursor.close()

