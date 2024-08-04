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
        cursor.execute(f"CREATE DATABASE {DB_NAME}")
        print(f"Database '{DB_NAME}' created successfully!")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:
            print(f"Database '{DB_NAME}' already exists.")
        else:
            print(f"Failed creating database: {err}")

def main():
    try:
        # Connect to MySQL server
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        # Create the database
        create_database(cursor)

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if cnx:
            cnx.close()

if __name__ == "__main__":
    main()
