import json
import psycopg2
from database_connect_class import DatabaseConnect

create_tbl = "create table target_table(c1 int, c2 int, primary key (c1))"
insert_data = "insert into target_table select generate_series(1, 10000000);"

query = [
    """
    set enable_nestloop = on;
    update target_table set c2 = from source_table where target_table.c1= source_table.c1;
    """
]

db_obj = DatabaseConnect()
con = None

try:

    con = db_obj.db_connect()

    con.autocommit = True
    cursor = con.cursor()
    for i in range(len(query)):
        cursor.execute(query[i])
    

except (Exception, psycopg2.DatabaseError) as error:
        print(error)

finally:
    if con:
        con.close()
        cursor.close()
