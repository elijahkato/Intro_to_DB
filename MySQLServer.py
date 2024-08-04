import mysql.connector
from mysql.connector import errorcode

# Database configuration
config = {
    'user': 'kato',
    'password': 'privatepass',
    'host': 'localhost',
}

# Database name
DB_NAME = 'alx_book_store'

def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")

def main():
    try:
        # Connect to MySQL server
        myConnection = mysql.connector.connect(**config)
        cursor = myConnection.cursor()

        # Create the database
        create_database(cursor)

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if myConnection:
            myConnection.close()

if __name__ == "__main__":
    main()
