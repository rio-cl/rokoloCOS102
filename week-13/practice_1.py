#connecting to a database
import psycopg2

# Database connection parameters
host = "localhost"
port = "5432"
dbname = "cos101_db"
user = "postgres"
password = "cos101"

# Establish the connection
try:
    connections = psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password
    )
    print("Connection to PostgreSQL DB successful")

    # Create a cursor object
    cursor = connections.cursor()

    # Execute a SQL query
    cursor.execute("SELECT version[];")

    # Fetch and print the result of the query
    db_version = cursor.fetchone()
    print(f"PostgreSQL database version: {db_version}")

    # Close the cursor and connection
    cursor.close()
    connections.close()

except Exception as error:
    print(f"Error connecting to PostgreSQL DB: {error}")
