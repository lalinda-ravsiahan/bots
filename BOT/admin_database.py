import mysql.connector
from mysql.connector import Error

async def create_connection(): #creating connecting with the mysql database
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
    
async def insert_admin_data(admin, drive_link,template_drive_link,required_responses):#inserting data into our admin_data database

    connection=create_connection

    try:
        cursor = connection.cursor()
        insert_query = '''
        INSERT INTO admin_data (admin, drive_link,template_drive_link,required_responses)
        VALUES (%s, %s,%s.%s)
        '''
        cursor.execute(insert_query, (admin, drive_link,template_drive_link,required_responses))
        connection.commit()
        print(f"User {admin} inserted successfully")
    except Error as e:
        print("Error while inserting data", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

async def get_form_drive_link(admin):#fetch the from drive link from the admin_data database for a prticutar admin id
    connection= create_connection

    try:
        cursor = connection.cursor()
        select_query = "SELECT form_drive_link FROM admin_data WHERE admin=%s"
        cursor.execute(select_query,(admin))
        result = cursor.fetchall()
        print(result)
    except Error as e:
        print("Error while fetching data", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

async def get_required_responses(admin):#fetch the required_responses from the admin_data database for a prticutar admin id
    connection= create_connection

    try:
        cursor = connection.cursor()
        select_query = "SELECT required_responses FROM admin_data WHERE admin=%s"
        cursor.execute(select_query,(admin))
        result = cursor.fetchall()
        return result
    except Error as e:
        print("Error while fetching data", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


#connection = create_connection()
#if connection:
    #get_form_drive_link(connection,5,17)