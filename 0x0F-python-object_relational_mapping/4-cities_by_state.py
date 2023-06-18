#!/usr/bin/python3
"""Select & print all cities in cities tables.
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
    cursor.execute("""
        SELECT cities.id, cities.name, states.name
        FROM `cities`,`states`
        WHERE cities.state_id = states.id""")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()
