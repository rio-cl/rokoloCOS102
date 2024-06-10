#selecting existing database
import psycopg2

# Database connection parameters
host = "localhost"
port = "5432"
dbname = "cos101_db"
user = "postgres"
password = "cos101"

# Establish the connection
try:
    connection = psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password
    )
    print("Connection to PostgreSQL DB successful")

    # Create a cursor object
    cursor = connection.cursor()

    # Define the SQL SELECT query
    select_query = "SELECT * FROM company;"

    # Execute the query
    cursor.execute(select_query)

    # Fetch all rows from the executed query
    data = cursor.fetchall()

    print("column", " | ", "column2")
    print("------------------------")

    # Iterate through the rows and print them
    for row in data:
        print(f"{row[0]}       |  {row[1]}")

    # Close the cursor and connection
    cursor.close()
    connection.close()

except Exception as error:
    print(f"Error connecting to PostgreSQL DB: {error}")
