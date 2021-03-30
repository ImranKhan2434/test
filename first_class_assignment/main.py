import psycopg2
import json
from database_connect_class import DatabaseConnect
from psycopg2 import extras

with open('data/data.json') as file_obj:
    data_json = json.load(file_obj)


class DatabaseOperation():
    def __init__(self):
        self.db_obj = DatabaseConnect()
        self.conn = self.db_obj.db_connect()
        self.cursor = self.conn.cursor()
        self.conn.autocommit = True

    def create_table(self):
        query = """
                CREATE TABLE data_info(
                    uuid VARCHAR(50) PRIMARY KEY,
                    data VARCHAR(100) NOT NULL,
                    min VARCHAR(100) NOT NULL,
                    max VARCHAR(100) NOT NULL,
                    avg VARCHAR(100) NOT NULL
                )
                """
        self.cursor.execute(query)
        print("Table is Created..")
        

    def insert_data_on_conflict(self):
        query = """
                INSERT INTO
                    data_info(uuid, data, min, max, avg) 
                VALUES (%s,%s,%s,%s,%s)
                ON CONFLICT (uuid) DO NOTHING
        """
        uuid, data, min, max, avg = data_json[0].values()
        self.cursor.execute(query, (uuid, data, min, max, avg))
        print("Data is Inserted..")


    def bulk_insert(self):
        query = """
                INSERT INTO 
                    data_info
                VALUES(
                    %(uuid)s, %(data)s, %(min)s, %(max)s, %(avg)s
                )
                ON CONFLICT DO NOTHING 
        """
        psycopg2.extras.execute_batch(self.cursor, query, data_json)
        print("Data is Inserted..")


    def update_data_on_conflict(self):
        pass

try:
    obj = DatabaseOperation()

    while True:
        print("Which operation do you want to perform on database? ")
        print("1. Create Database\n2. Insert Data\n3. Update Data\n4. Bulk Insert\n5. Exit")
        print("Please enter the option code: ")
        n = input()

        if (n == '1'):
            obj.create_table()
        elif (n == '2'):
            obj.insert_data_on_conflict()
        elif (n == '3'):
            obj.update_data_on_conflict()
        elif (n == '4'):
           obj.bulk_insert()
        elif (n == '5'):
           break
        else:
            print("This is not an option code..!!\nPlease try aggain.")
            break



except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if obj.conn:
        obj.cursor.close()
        obj.conn.close()