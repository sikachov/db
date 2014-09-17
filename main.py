__author__ = 'evgeny'

import MySQLdb


db = MySQLdb.connect("localhost", "evgeny", "sikachov")


def do_sql(command):
    cursor = db.cursor()
    cursor.execute(command)
    return cursor.fetchone()


def close_connection(database):
    database.close()


print "Database version : %s " % do_sql("SELECT VERSION()")

close_connection(db)