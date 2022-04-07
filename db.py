import mysql.connector

#from coronisecrets import hostname, username, password, datab
from helpers.db_create import create_database

hostname = "localhost"
username = "root"
password = "password"
datab = "coronacentre"

mydb = mysql.connector.connect(
    host = hostname,
    user = username,
    passwd = password,
    database = datab,
)

my_cursor = mydb.cursor(buffered=True)

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

def query(query):
    #my_cursor.execute("USE coronacentre")
    my_cursor.execute(query)
    mydb.commit()
    #for db in my_cursor:
        #print(db)
    return my_cursor.fetchall()