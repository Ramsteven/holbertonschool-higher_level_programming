#!/usr/bin/python3
"""
modulete get all
"""
import MySQLdb
from sys import argv

if len(argv) is 4:
    db = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC;")
    rows = c.fetchall()
    for eachRow in rows:
        print(eachRow)
    cursor.close()
    db.close()
