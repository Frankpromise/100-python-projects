import psycopg2

#Connect to PostgreSQL from Python
try:
    connection = psycopg2.connect(user="USER",
                                  password="PASSWORD",
                                  port="5432",
                                  host="host",
                                  database="db_name")
    
#Get Cursor Object from Connection and Define a PostgreSQL SELECT Query 
    cursor = connection.cursor()
    postgresql_select_query = "select * from db_name"
    

#Execute the SELECT query using a execute() method and Extract all rows
    cursor.execute(postgresql_select_query)
    print("Selecting rows from db_name table using cursor.fetchall")
    db_record = cursor.fetchall
    

#Iterate each row
    print("display each row and its corresponding columns in the table")
    for row in db_record:
        print("Id = ", row[0], )
        print("name = ", row[1])
        

except (Exception, psycopg2.Error) as error:
    print("Error fetching data from postgresql", error)


#Close the cursor object and database connection object
finally:
    if connection:
        cursor.close()
        connection.close()
        print("postgresql connection is closed")