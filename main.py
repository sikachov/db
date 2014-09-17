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


while (1):
    choice=int(raw_input("1.Add user\n 2.Show db\n 3.Show tables"))
    if choice==3:
        print do_sql("show all")
print "Database version : %s " % do_sql("SELECT VERSION()")

close_connection(db)

