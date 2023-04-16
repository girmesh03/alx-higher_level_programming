#!/usr/bin/python3
"""
Write a script that takes in arguments and displays all
values in the states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!

Your script should take 4 arguments: mysql username,
mysql password, database name and state name searched
(safe from MySQL injection)

You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on
localhost at port 3306
Results must be sorted in ascending order by states.id
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()

    # Execute parameterized query
    query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
    cur.execute(query, (argv[4],))

    # Fetch and display results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close connections
    cur.close()
    db.close()
