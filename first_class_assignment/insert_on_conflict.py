import json
import psycopg2
from database_connect_class import DatabaseConnect

keys = []

# Read json file and store it into python obj(Dictionary)
with open('data/data.json') as file_obj:
    data_json = json.load(file_obj)

for row in data_json:
    for key in row:
        if key not in keys:
            keys.append(key)


len_dict = len(data_json)

# Create database table query
create_tbl = """
        CREATE TABLE data_info(
            uuid VARCHAR(50) PRIMARY KEY,
            data VARCHAR(100) NOT NULL,
            min VARCHAR(100) NOT NULL,
            max VARCHAR(100) NOT NULL,
            avg VARCHAR(100) NOT NULL
        )
    """
# Insert query to insert data into database table
query = """
                INSERT INTO 
                    student_info(std_name, email)
                VALUES(
                    'Imran Khan',
                    'duetboyimran@gmail.com'
                )
                ON CONFLICT (std_name) DO NOTHING
    """

# Initialize DatabasseConnect class
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
    cursor.execute(query)
    print("Data is Inserted into Student Info..")

except (Exception, psycopg2.DatabaseError) as error:
        print(error)

finally:
    if conn:
        conn.close()
        cursor.close()


