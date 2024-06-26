#!/usr/bin/python3

'''
This module show all states from the database given trough command line
'''

# Establish connection to MySQL database using command-line arguments
import MySQLdb  # Import MySQLdb library for MySQL database interaction
import sys  # Import sys module for accessing command-line arguments


def get_states():
    """
    Connects to a MySQL database and retrieves all states
    from the 'states' table.

    Assumes MySQL username, password, and database name are 0
    provided as command-line arguments.
    """
    conn = MySQLdb.connect(
        host="localhost",  # server host
        port=3306,  # server port
        user=sys.argv[1],  # username (provided as command-line argument)
        passwd=sys.argv[2],  # password (provided as command-line argument)
        db=sys.argv[3],  # database name (provided as command-line argument)
        charset="utf8"  # Character encoding for the connection
    )

    # Create a cursor object to execute SQL queries
    cur = conn.cursor()

    # Execute SQL query to select states starting with 'N'
    cur.execute("SELECT * FROM states WHERE BINARY name LIKE\
                 'N%' ORDER BY id ASC")

    # Fetch all rows from the executed query
    query_rows = cur.fetchall()

    # Iterate over fetched rows and print each row
    for row in query_rows:
        print(row)

    # Close the cursor to release resources
    cur.close()

    # Close the database connection
    conn.close()


if __name__ == '__main__':
    get_states()
