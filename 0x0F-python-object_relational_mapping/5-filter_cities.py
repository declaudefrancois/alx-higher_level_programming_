#!/usr/bin/python3
"""Filter states query.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cur = conn.cursor()

    sql = ("SELECT c.name FROM cities AS c, states AS s "
           "WHERE c.state_id = s.id  AND s.name = %s "
           "ORDER BY c.id ASC")

    cur.execute(sql, (sys.argv[4],))
    rows = list(cur.fetchall())
    rows = [item[0] for item in rows]
    print(", ".join(rows))

    cur.close()
    conn.close()
