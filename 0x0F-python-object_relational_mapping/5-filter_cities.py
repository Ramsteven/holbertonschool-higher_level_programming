#!/usr/bin/python3
''' script that takes in an argument and display all values'''

import MySQLdb
from sys import argv

if len(argv) is 5:
    db = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )

    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities \
    LEFT JOIN states ON cities.state_id = states.id \
    WHERE states.name = '%s' \
    ORDER BY cities.id;" % argv[4])
    rows = cursor.fetchall()
    list_ = []
    for row in cursor:
        list_.append(row[0])
    print(", ".join(list_))
    cursor.close()
