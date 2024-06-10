# Inserting into table
import psycopg2

# Database connection parameters
host = "localhost"
port = "5432"
dbname = "cos102_db"
user = "postgres"
password = "cos101"

try:
    # Connect to the PostgreSQL database
    connection = psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password
    )
    connection.autocommit = True  # Enable autocommit mode
    print("Connection to PostgreSQL DB successful")

    # Create a cursor object
    cursor = connection.cursor()

    # Define the SQL INSERT statement
    insert_query = """
    INSERT INTO sst_info (id, name, age, department, password)
    VALUES (%s, %s, %s, %s, %s);
    """

    # Data to be inserted
    data_to_insert = [
        (1, "Jamel Ojo", 20, "Software Engineering", "anthelo4"),
        (2, "Jamal Okon", 22, "Software Engineering", "jokon")
    ]

    # Execute the SQL statement
    cursor.execute(insert_query, data_to_insert)
    print("Data inserted successfully")

    # Close the cursor and connection
    cursor.close()
    connection.close()

except Exception as error:
    print(f"Error inserting data: {error}")
