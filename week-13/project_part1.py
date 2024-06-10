import psycopg2
from psycopg2 import sql

host = "localhost"
port = "5432"
dbname = "cos101_db"
user = "postgres"
password = "cos101"

new_dbname = "Paystack_Team1.1"

try:
    connection = psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password
    )
    connection.autocommit = True  # Enable autocommit mode
    print("Connection to PostgreSQL server successful")

    cursor = connection.cursor()

    create_db_query = sql.SQL("CREATE DATABASE {}").format(sql.Identifier(new_dbname))

    cursor.execute(create_db_query)
    print(f"Database '{new_dbname}' created successfully")
    
    # Close the cursor and connection
    cursor.close()
    connection.close()

except Exception as error:
    print(f"Error creating the database: {error}")





