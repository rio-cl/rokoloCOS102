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

    insert_query = """
    INSERT INTO paystack (id, name, department, age, module)
    VALUES (%s, %s, %s, %s, %s);
    """

    data_to_insert1 = (1, "Oyinda Aina", "Business", 32, 1)
    data_to_insert2 = (2, "Wale Eseyin", "Engineering", 28, 3)
    data_to_insert3 = (3, "Khadija Abu", "Product", 30, 2)
    data_to_insert4 = (4, "Onyekachi Mbaike", "Design", 37, 5)
    data_to_insert5 = (5, "Seike Ibijo", "Growth", 33, 4)
    data_to_insert6 = (6, "Opemipo Aikomo", "Design", 28, 1)
    data_to_insert7 = (7, "Ezra Olubi", "Product", 30, 3)
    data_to_insert8 = (8, "Alexander Fasoro", "Engineering", 35, 1)
    data_to_insert9 = (9, "Stephen Amaza", "Growth", 40, 2)
    data_to_insert10 = (10, "Loknan Nanyak", "Engineering", 44, 5)
    data_to_insert11 = (11, "Ibrahim Lawal", "Engineering", 39, 4)
    data_to_insert12 = (12, "Fisayo Kolawole", "Commercial", 27, 5)
    data_to_insert13 = (13, "Emmanuel Quatrey", "Growth", 31, 1)
    data_to_insert14 = (14, "Awatt Basey", "Growth", 32, 2)
    data_to_insert15 = (15, "Bolaji Akande", "Revenue", 30, 3)
    data_to_insert16 = (16, "Mohini Ufeli", "Grwoth", 29, 1)
    data_to_insert17 = (17, "King Makanjuola", "Product", 31, 4)
    data_to_insert18 = (18, "Ijeoma Opara", "Revenue", 26, 2)
    data_to_insert19 = (19, "Dipo Omobomi", "Product", 32, 5)
    data_to_insert20 = (20, "Dapo Awombokun", "Revenue", 35, 3)
    data_to_insert21 = (21, "Charles Ibem", "Revenue", 38, 1)
    data_to_insert22 = (22, "Ayobami Alo", "Product", 34, 4)
    data_to_insert23 = (23, "Aminat Badara", "Growth", 30, 2)

    cursor.execute(insert_query, data_to_insert2)
    cursor.execute(insert_query, data_to_insert3)
    cursor.execute(insert_query, data_to_insert4)
    cursor.execute(insert_query, data_to_insert5)
    cursor.execute(insert_query, data_to_insert6)
    cursor.execute(insert_query, data_to_insert7)
    cursor.execute(insert_query, data_to_insert8)
    cursor.execute(insert_query, data_to_insert9)
    cursor.execute(insert_query, data_to_insert10)
    cursor.execute(insert_query, data_to_insert11)
    cursor.execute(insert_query, data_to_insert12)
    cursor.execute(insert_query, data_to_insert13)
    cursor.execute(insert_query, data_to_insert14)
    cursor.execute(insert_query, data_to_insert15)
    cursor.execute(insert_query, data_to_insert16)
    cursor.execute(insert_query, data_to_insert17)
    cursor.execute(insert_query, data_to_insert18)
    cursor.execute(insert_query, data_to_insert19)
    cursor.execute(insert_query, data_to_insert20)
    cursor.execute(insert_query, data_to_insert21)
    cursor.execute(insert_query, data_to_insert22)
    cursor.execute(insert_query, data_to_insert23)

    print("Data inserted successfully")

    # Close the cursor and connection
    cursor.close()
    connection.close()

except Exception as error:
    print(f"Error inserting data: {error}")
