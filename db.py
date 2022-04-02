import mysql.connector

from secrets import hostname, username, password
from helpers.db_create import create_database

mydb = mysql.connector.connect(
    host = hostname,
    user = username,
    passwd = password,
)

my_cursor = mydb.cursor()

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    if "coronacentre" in db:
        db_exist = True
        break
    else:
        db_exist = False

if db_exist == False:
    print("Datenbank existiert noch nicht. DB wird nun erstellt.")
    create_database()
else:
    print("Datebank existiert bereits.")

#def pull(query):
#    my_cursor.execute(query)
#    for db in my_cursor:
#        #print(db)
#        return db