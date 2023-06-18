#!/usr/bin/python3
"""Select & print all states in states tables.
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    user = sys.argv[1]
    pswd = sys.argv[2]
    db = sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=pswd,
        db=db,
        charset="utf8"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `states`")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()
