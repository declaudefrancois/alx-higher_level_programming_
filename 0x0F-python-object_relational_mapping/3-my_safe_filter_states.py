#!/usr/bin/python3
""" lists all states which macth the fourth command line arguments.
    take 4 arguments: mysql username, mysql password, database name
    and state name searched.
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    user = sys.argv[1]
    pswd = sys.argv[2]
    db = sys.argv[3]
    term = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=pswd,
        db=db,
        charset="utf8"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `states` WHERE name LIKE %s", (term,))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()
