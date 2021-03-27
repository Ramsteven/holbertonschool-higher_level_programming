#!/usr/bin/python3
''' script that takes in an argument and display all values'''

import MySQLdb
from sys import argv

if __name__ == '__main__':

    try:
        db = MySQLdb.connect(
            host='localhost',
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            port=3306
        )

        cursor = db.cursor()
        cursor.execute("SELECT id, name FROM states \
        WHERE name LIKE %s \
        ORDER BY states.id ASC;", (argv[4],))
        rows = cursor.fetchall()
        for row in cursor:
            print(row)
        cursor.close() 
    except Exception as err:
        print(err)
        pass
