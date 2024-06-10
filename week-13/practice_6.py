# Selecting from a table
import psycopg2

# Define your database connection parameters
db_params = {
    'dbname': 'cos102_db',
    'user': 'postgres',
    'password': 'cos101',
    'host': 'localhost',
    'port': '5432'  # Default is '5432'
}

try:
    # Establish a connection to the database
    connection = psycopg2.connect(**db_params)

    # Create a cursor object
    cursor = connection.cursor()

    # Define the SQL query
    select_query = "SELECT * FROM sst_info WHERE age < 30"
    select_query2 = "SELECT * FROM sst_info WHERE age > 30"

    # Execute the SQL query
    cursor.execute(select_query)

    # Fetch all the results
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)


except Exception as error:
    print(f"Error while connecting to PostgreSQL: {error}")

finally:
    # Close the cursor and connection to clean up
    if cursor:
        cursor.close()
    if connection:
        connection.close()
