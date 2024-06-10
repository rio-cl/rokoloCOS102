# Creating new database
import psycopg2
from psycopg2 import sql

# Parameters to connect to the existing PostgreSQL server
host = "localhost"
port = "5432"
dbname = "cos101_db"
user = "postgres"
password = "cos101"
# Connect to the default database

# Name of the new database to be created
new_dbname = "cos102_db"

try:
    # Connect to the PostgreSQL server
    connection = psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password
    )
    connection.autocommit = True  # Enable autocommit mode
    print("Connection to PostgreSQL server successful")

    # Create a cursor object
    cursor = connection.cursor()

    # Define the SQL statement to create a new database
    create_db_query = sql.SQL("CREATE DATABASE {}").format(sql.Identifier(new_dbname))

    # Execute the SQL statement
    cursor.execute(create_db_query)
    print(f"Database '{new_dbname}' created successfully")

    # Close the cursor and connection
    cursor.close()
    connection.close()

except Exception as error:
    print(f"Error creating the database: {error}")
