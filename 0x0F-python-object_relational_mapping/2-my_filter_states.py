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
    )

    cursor = conn.cursor()
    sql = """
            SELECT * FROM `states`
            WHERE name LIKE BINARY '{}'
            ORDER BY states.id ASC
        """
    cursor.execute(sql.format(term))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()
