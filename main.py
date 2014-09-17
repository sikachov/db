__author__ = 'evgeny'

import psycopg2


try:
    db = psycopg2.connect("dbname='users' user='evgeny' host='localhost' password='sikachov'")
except:
    print "I am unable to connect to the database"


def do_sql(command):
    cursor = db.cursor()
    cursor.execute(command)
    return cursor.fetchall()


def close_connection(database):
    database.close()


print "Database version : %s " % do_sql("SELECT VERSION()")

close_connection(db)

