import mysql.connector

from secrets import hostname, username, password

mydb = mysql.connector.connect(
    host = hostname,
    user = username,
    passwd = password,
)

my_cursor = mydb.cursor()

def create_database():
    my_cursor.execute("CREATE DATABASE coronacentre")
    my_cursor.execute("USE coronacentre")

    my_cursor.execute("""CREATE TABLE vax_status(
        status_id INT AUTO_INCREMENT PRIMARY KEY,
        impf_count INT,
        rec_count INT,
        last_impf DATE,
        last_rec DATE
        )""")

    my_cursor.execute("""CREATE TABLE address(
        address_id INT AUTO_INCREMENT PRIMARY KEY, 
        housenumber INT,
        street VARCHAR(100),
        plz INT,
        city VARCHAR(100),
        state VARCHAR(100),
        country VARCHAR(100)
        )""")

    my_cursor.execute("""CREATE TABLE customers(
        customer_id INT PRIMARY KEY,
        surname VARCHAR(100),
        name VARCHAR(100),
        birthday DATE,
        address_id INT,
        status_id INT,
        FOREIGN KEY (status_id) REFERENCES vax_status(status_id),
        FOREIGN KEY(address_id) REFERENCES address(address_id)
        )""")

    my_cursor.execute("""CREATE TABLE test_appoints(
        appoints_id INT AUTO_INCREMENT PRIMARY KEY,
        customer_id INT,
        empl_id INT, datetime TIMESTAMP,
        result VARCHAR(100),
        FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
        )""")

    my_cursor.execute("""CREATE TABLE test_type(
        testtype_nr INT AUTO_INCREMENT PRIMARY KEY,
        testmethod VARCHAR(100),
        price DECIMAL(10,0)
        )""")

    my_cursor.execute("""CREATE TABLE appoint_type(
        appoints_id INT,
        testtype_nr INT,
        FOREIGN KEY(appoints_id) REFERENCES test_appoints(appoints_id),
        FOREIGN KEY(testtype_nr) REFERENCES test_type(testtype_nr)
        )""")

    my_cursor.execute("""CREATE TABLE employees(
        empl_id INT AUTO_INCREMENT PRIMARY KEY,
        surname VARCHAR(30),
        name VARCHAR(30),
        birthday DATE,
        address_id INT,
        FOREIGN KEY(address_id) REFERENCES address(address_id)
        )""")

    my_cursor.execute("""CREATE TABLE vaccination(
        impf_id INT AUTO_INCREMENT PRIMARY KEY,
        vaccine VARCHAR(100)
        )""")

    my_cursor.execute("""CREATE TABLE vax_appoints(
        customer_id INT,
        empl_id INT,
        datetime TIMESTAMP,
        impf_id INT,
        FOREIGN KEY(impf_id) REFERENCES vaccination(impf_id),
        FOREIGN KEY(empl_id) REFERENCES employees(empl_id),
        FOREIGN KEY(customer_id) REFERENCES customers (customer_id)
        )""")

    print("Datenbank wurde erstellt.")