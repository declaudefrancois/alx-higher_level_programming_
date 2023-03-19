#!/usr/bin/python3
"""Get all states query.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    pswd = sys.argv[2]
    db = sys.argv[3]
    conn = MySQLdb.connect(
        host="localhost",
        port=3306, user=user,
        passwd=pswd,
        db=db,
        charset="utf8"
    )
    cur = conn.cursor()

    cur.execute("SELECT * FROM `states` ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
