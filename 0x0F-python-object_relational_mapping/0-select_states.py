#!/usr/bin/python3
"""
Module
"""
import MySQLdb
from sys import argv

db = MySQLdb.connect(
    host='localhost',
    user=argv[1],
    passwd=argv[2],
    db=argv[3],
    port=3306)

cursor = db.cursor()

cursor.execute("SELECT * FROM states ORDER BY id;")
rows = cursor.fetchall()
for id_query in rows:
    print("{}".format(id_query))
cursor.close()
db.close()
