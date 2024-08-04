import mysql.connector
from mysql.connector import errorcode

# Database configuration
config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
}

# Database name
DB_NAME = 'alx_book_store'

def create_database(cursor):
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        print(f"Database '{DB_NAME}' created successfully!")
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
