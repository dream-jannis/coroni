import mysql.connector
#from helpers.db_create import create_database
#from coronisecrets import hostname, username, password,datab

hostname = "localhost"
username = "root"
password = "password"
#datab = "coronacentre"

mydb = mysql.connector.connect(
    host = hostname,
    user = username,
    passwd = password,
    #database = datab,
)

my_cursor = mydb.cursor()

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    if "coronacentre" in db:
        db_exist = True
        break
    else:
        db_exist = False



def create_database():
    my_cursor.execute("CREATE DATABASE coronacentre")
    my_cursor.execute("use coronacentre")

    my_cursor.execute("""
        CREATE TABLE vax_status(
            status_id INT AUTO_INCREMENT PRIMARY KEY,
            impf_count INT,
            rec_count INT,
            last_impf DATE,
            last_rec DATE
        )""")

    my_cursor.execute("""
        CREATE TABLE address(
            address_id INT AUTO_INCREMENT PRIMARY KEY, 
            housenumber INT,
            street VARCHAR(100),
            plz INT,
            city VARCHAR(100),
            state VARCHAR(100),
            country VARCHAR(100)
        )""")

    my_cursor.execute("""
        CREATE TABLE user(
            user_id INT AUTO_INCREMENT PRIMARY KEY,
            surname VARCHAR(100),
            name VARCHAR(100),
            email VARCHAR(100),
            password VARCHAR(100),
            birthday DATE,
            is_admin BOOLEAN,
            address_id INT,
            status_id INT,

            FOREIGN KEY (status_id) REFERENCES vax_status(status_id),
            FOREIGN KEY(address_id) REFERENCES address(address_id)
        )""")

    my_cursor.execute("""
        CREATE TABLE test_type(     
            testtype_nr INT AUTO_INCREMENT PRIMARY KEY,
            testmethod VARCHAR(100),
            price DECIMAL(10,0)
        )""")

    my_cursor.execute("""
        CREATE TABLE test_appoints(
            appoints_id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            datetime TIMESTAMP,
            testtype_nr INT,
            result VARCHAR(100),

            FOREIGN KEY(testtype_nr) REFERENCES test_type(testtype_nr),
            FOREIGN KEY(user_id) REFERENCES user(user_id)
        )""")

    my_cursor.execute("""
        CREATE TABLE appoint_type(
            appoints_id INT,
            testtype_nr INT,
        
            FOREIGN KEY(appoints_id) REFERENCES test_appoints(appoints_id),
            FOREIGN KEY(testtype_nr) REFERENCES test_type(testtype_nr)
        )""")

    my_cursor.execute("""
        CREATE TABLE vaccination(
            impf_id INT AUTO_INCREMENT PRIMARY KEY,
            vaccine VARCHAR(100)
        )""")

    my_cursor.execute("""
        CREATE TABLE vax_appoints(
            user_id INT,
            datetime TIMESTAMP,
            impf_id INT,

            FOREIGN KEY(impf_id) REFERENCES vaccination(impf_id),
            FOREIGN KEY(user_id) REFERENCES user (user_id)
        )""")

    my_cursor.execute("""
        INSERT INTO test_type(
            testmethod, price
        ) VALUES (
            "Schnelltest", '0'
        )
    """)
    my_cursor.execute("""
        INSERT INTO test_type(
            testmethod, price
        ) VALUES (
            "PCR-Test", '50'
        )
    """)
    my_cursor.execute("""
        INSERT INTO test_type(
            testmethod, price
        ) VALUES (
            "AntiGen-Test", '30'
        )
    """)
    mydb.commit()

    print("Datenbank wurde erstellt.")


if db_exist == False:
    print("Datenbank existiert noch nicht. DB wird nun erstellt.")
    create_database()
else:
    print("Datebank existiert bereits.")