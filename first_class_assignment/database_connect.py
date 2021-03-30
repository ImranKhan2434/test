import psycopg2
from psycopg2 import Error

# use psycopg2.connect() method to connect mysql that returns an object if the connection is successful.
connection = psycopg2.connect(
    host='localhost',
    database='test',
    user='postgres',
    password='postgres',
    port='5432'
)

try:
    # Create cursor obj to perform query operations.
    cursor = connection.cursor()
    query = "SELECT version()"
    cursor.execute(query)
    query_result = cursor.fetchone()
    print("You are connected to - ", query_result)

except(Exception, Error):
    print(Error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed!")