#!/usr/bin/python3

"""
Write a script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.

Your script should take 4 arguments: mysql username,
mysql password, database name and state name searched
(no argument validation needed)

You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
You must use format to create the SQL query with the user input
Results must be sorted in ascending order by states.id
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Establish a connection to the database
    conn = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
    )

    # Create a cursor object
    cur = conn.cursor()

    # Execute the SQL query to retrieve states
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    state_name = sys.argv[4]
    cur.execute(query, (state_name,))

    # Print the results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    conn.close()
