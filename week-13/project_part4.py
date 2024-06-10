# Selecting from a table
import psycopg2

# Define your database connection parameters
db_params = {
    'dbname': 'Paystack_Team1.1',
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
    #select_query1 = "SELECT name FROM paystack WHERE (department = 'Revenue')"
    #select_query2 = "SELECT name FROM paystack WHERE ((department = 'Growth') and (department = 'Product') and (age > 30) and(age < 35))"
    select_query3 = "SELECT name FROM paystack WHERE (module = 1)"
    select_query4 = "SELECT name FROM paystack WHERE (age > 30)"
    #select_query5 = "SELECT name FROM paystack WHERE (module = 5)"
    #select_query4 = "SELECT name FROM paystack WHERE ((module = 4) and (department = 'Product'))"

    # Execute the SQL query
    #cursor.execute(select_query1)
    #cursor.execute(select_query2)
    cursor.execute(select_query3)
    cursor.execute(select_query4)
    #cursor.execute(select_query5)

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
