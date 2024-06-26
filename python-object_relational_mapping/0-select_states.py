import MySQLdb  # Import MySQLdb library for MySQL database interaction
import sys  # Import sys module for accessing command-line arguments

# Establish connection to MySQL database using command-line arguments
conn = MySQLdb.connect(
    host="localhost",  # MySQL server host
    port=3306,  # MySQL server port
    user=sys.argv[1],  # MySQL username (provided as command-line argument)
    passwd=sys.argv[2],  # MySQL password (provided as command-line argument)
    db=sys.argv[3],  # MySQL database name (provided as command-line argument)
    charset="utf8"  # Character encoding for the connection
)

# Create a cursor object to execute SQL queries
cur = conn.cursor()

# Execute SQL query to select all rows from the 'states' table
cur.execute("SELECT * FROM states ORDER BY id ASC")

# Fetch all rows from the executed query
query_rows = cur.fetchall()

# Iterate over fetched rows and print each row
for row in query_rows:
    print(row)

# Close the cursor to release resources
cur.close()

# Close the database connection
conn.close()
