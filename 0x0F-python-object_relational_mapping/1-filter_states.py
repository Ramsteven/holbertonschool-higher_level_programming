#!/usr/bin/python3
''' script that starging all with N '''

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
        query = "SELECT id, name FROM states \
        WHERE name LIKE BINARY 'N%' ORDER BY id ASC;"
        cursor.execute(query)
        #rows = cursor.fetchall()
        for result in cursor:
            print(result)
        cursor.close() 
    except Exception:
        pass
