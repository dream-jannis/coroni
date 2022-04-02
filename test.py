import mysql.connector

from secrets import hostname, username, password
from db import pull

mydb = mysql.connector.connect(
    host = hostname,
    user = username,
    passwd = password,
)

my_cursor = mydb.cursor()


def pull():
    my_cursor.execute("USE coronacentre")
    my_cursor.execute("SELECT * FROM address")
    for db in my_cursor:
        print(db)
pull()

#query = "SELECT * FROM address"

#pull(query)