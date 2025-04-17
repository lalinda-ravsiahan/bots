import mysql.connector
from mysql.connector import Error

def create_connection(): #creating connecting with the mysql database
    try:
        connection = mysql.connector.connect(
            host='localhost',       # MySQL server address
            database='birth',      # Database name
            user='root',            # MySQL username
            password='leeshar2002'     # MySQL password
        )
        if connection.is_connected():
            print("Successfully connected to the database")
            return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None
    
def insert_data(connection, name, month, day):#inserting data into our sql database
    try:
        cursor = connection.cursor()
        insert_query = '''
        INSERT INTO details (name, month, day)
        VALUES (%s, %s, %s)
        '''
        cursor.execute(insert_query, (name, month, day))
        connection.commit()
        print(f"User {name} inserted successfully")
    except Error as e:
        print("Error while inserting data", e)

def fetch_user_data(connection,month,day):
    try:
        cursor = connection.cursor()
        select_query = "SELECT name FROM details WHERE month=%s AND day=%s"
        cursor.execute(select_query,(month,day))
        result = cursor.fetchall()
        print(result)
    except Error as e:
        print("Error while fetching data", e)


connection = create_connection()
if connection:
    #insert_data(connection, 'kojika dewanganai',5,17 )
    fetch_user_data(connection,5,17)