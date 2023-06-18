#!/usr/bin/python3
""" lists all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa.
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
    cursor.execute("SELECT * FROM `states` WHERE name LIKE BINARY 'N%'")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()
