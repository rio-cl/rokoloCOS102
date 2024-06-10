import psycopg2

# Database connection parameters
host = "localhost"
port = "5432"
dbname = "Paystack_Team1.1"
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

    create_table_query = """
    CREATE TABLE paystack (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        department VARCHAR NOT NULL,
        age INT NOT NULL,
        module INT NOT NULL
    );
    """
    cursor.execute(create_table_query)
    print("Table created successfully")

    # Close the cursor and connection
    cursor.close()
    connection.close()

except Exception as error:
    print(f"Error creating table: {error}")
