#!/usr/bin/python3
"""Takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa.
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    user = sys.argv[1]
    pswd = sys.argv[2]
    db = sys.argv[3]
    city = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=pswd,
        db=db,
    )

    cursor = conn.cursor()
    sql = """
        SELECT cities.name
        FROM `cities`
        INNER JOIN `states` ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC"""
    cursor.execute(sql, (city,))
    rows = cursor.fetchall()
    rows_count = len(rows)
    for i in range(rows_count):
        print(
            "{}".format(rows[i][0]),
            end=(", " if i < rows_count - 1 else "\n")
        )

    # Empty line
    if rows_count == 0:
        print("")

    cursor.close()
    conn.close()
