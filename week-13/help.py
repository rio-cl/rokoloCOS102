create_db_query = sql.SQL("CREATE DATABASE {}").format(sql.Identifier(new_dbname))

    cursor.execute(create_db_query)
    print(f"Database '{new_dbname}' created successfully")

    create_table_query = """
    CREATE TABLE paystack (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        department VARCHAR NOT NULL,
        age INT NOT NULL,
        module INT NOT NULL
    );
    """

    insert_query = """
    INSERT INTO paystack (id, name, department, age, module)
    VALUES (%s, %s, %s, %s, %s);
    """

    data_to_insert = ((1, "Oyinda Aina", "Business", 32, 1),
                      (2, "Wale Eseyin", "Engineering", 28, 3),
                      (3, "Khadija Abu", "Product", 30, 2),
                      (4, "Onyekachi Mbaike", "Design", 37, 5),
                      (5, "Seike Ibijo", "Growth", 33, 4),
                      (6, "Opemipo Aikomo", "Design", 28, 1),
                      (7, "Ezra Olubi", "Product", 30, 3),
                      (8, "Alexander Fasoro", "Engineering", 35, 1),
                      (9, "Stephen Amaza", "Growth", 40, 2),
                      (10, "Loknan Nanyak", "Engineering", 44, 5),
                      (11, "Ibrahim Lawal", "Engineering", 39, 4),
                      (12, "Fisayo Kolawole", "Commercial", 27, 5),
                      (13, "Emmanuel Quatrey", "Growth", 31, 1),
                      (14, "Awatt Basey", "Growth", 32, 2),
                      (15, "Bolaji Akande", "Revenue", 30, 3),
                      (16, "Mohini Ufeli", "Grwoth", 29, 1),
                      (17, "King Makanjuola", "Product", 31, 4),
                      (18, "Ijeoma Opara", "Revenue", 26, 2),
                      (19, "Dipo Omobomi", "Product", 32, 5),
                      (20, "Dapo Awombokun", "Revenue", 35, 3),
                      (21, "Charles Ibem", "Revenue", 38, 1),
                      (22, "Ayobami Alo", "Product", 34, 4),
                      (23, "Aminat Badara", "Growth", 30, 2)
                      )

    select_query1 = "SELECT division FROM paystack WHERE (division == Revenue)"
    select_query2 = "SELECT division FROM paystack WHERE ((division == Growth) and (division == Product) and (age > 30) and(age < 35))"
    select_query3 = "SELECT division FROM paystack WHERE ((module = 1) and (module = 3) and (module = 5))"
    select_query4 = "SELECT division FROM paystack WHERE ((module = 4) and (division == Product))"

    cursor.execute(create_db_query)
    cursor.execute(create_table_query)
    cursor.execute(insert_query, data_to_insert)
    cursor.execute(select_query1, select_query2)
    cursor.execute(select_query3, select_query4)

    print(f"Database '{new_dbname}' created successfully\n")
    print("Data inserted successfully\n\n")
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    connection.close()


except Exception as error:
    print(f"Error inserting data: {error}")
