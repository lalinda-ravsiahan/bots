import mysql.connector
from mysql.connector import Error

#creating connecting with the mysql database
async def create_connection(): 
    try:
        connection = mysql.connector.connect(
            host='localhost',       # MySQL server address
            database='ucsc21',      # Database name
            user='root',            # MySQL username
            password='leeshar2002'     # MySQL password
        )
        if connection.is_connected():
            print("Successfully connected to the database")
            return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None
    
#creating seperate tables for every admin to store their birthday  data
async def create_birthday_table(admin):
    connection=create_connection
    try:
        cursor = connection.cursor()
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS {admin} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            month INT NOT NULL,
            date INT NOT NULL,
            photo_link VARCHAR(200) NOT NULL
        );
        '''
        cursor.execute(create_table_query)
        connection.commit()
        print("Table `users` created successfully")
    except Error as e:
        print("Error while creating table", e)
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


#inserting every admins birthday data into admins seperate database
async def insert_birthday_data(table_name,name, month,date,photo_link):
    connection=create_connection
    try:
        cursor = connection.cursor()
        insert_query = '''
        INSERT INTO {table_name} (name, month,date,photo_link)
        VALUES (%s, %s,%s,%s)
        '''
        cursor.execute(insert_query, (name, month,date,photo_link))
        connection.commit()
        print(f"User {name} inserted successfully")

    except Error as e:
        print("Error while inserting data", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

#fetch user data according to the month and date
async def fetch_users_birthday_data(month,date):
    connection=create_connection
    try:
        cursor = connection.cursor()
        select_query = "SELECT name FROM admin_data WHERE month=%s AND date=%s"
        cursor.execute(select_query,(month,date))
        result = cursor.fetchall()
        print(result)
    except Error as e:
        print("Error while fetching data", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


async def search_table(table_name):
    connection=connection.cursor()
    try:
        cursor=connection.cursor()
        cursor.execute("SHOW TABLES")
        
        # Fetch all tables
        tables = cursor.fetchall()

        # Check if the specified table exists
        for table in tables:
            if table[0] == table_name:
                return True
            
        return False
    
    except Error as e:
        print(f"Error: {e}")
        return False

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

connection = create_connection()
if connection:
    fetch_users_birthday_data(connection,5,17)