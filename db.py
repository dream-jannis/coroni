from logging import root
import mysql.connector


from coronisecrets import hostname, username, password, datab


def select_request(query):
    try:
        connection = mysql.connector.connect(host = hostname,
                                            user = username,
                                            passwd = password,
                                            database = datab, )
        my_cursor = connection.cursor()
        print("connected")
        my_cursor.execute(query)
        print("query ausgeführt")
        #connection.commit()
        row = my_cursor.fetchone()
        print("fetched")
        output = row
                
        
        print("success")
        my_cursor.close()

        return output

    except mysql.connector.Error as error:
        print("failed".format(error))
    
    finally:
        if connection.is_connected():
            connection.close()

def select_request_all(query):
    try:
        connection = mysql.connector.connect(host = hostname,
                                            user = username,
                                            passwd = password,
                                            database = datab, )
        my_cursor = connection.cursor()
        print("connected")
        my_cursor.execute(query)
        print("query ausgeführt")
        #connection.commit()
        row = my_cursor.fetchall()
        print("fetched")
        output = row
                
        
        print("success")
        my_cursor.close()

        return output

    except mysql.connector.Error as error:
        print("failed".format(error))
    
    finally:
        if connection.is_connected():
            connection.close()

def insert_request(query):
    try:
        connection = mysql.connector.connect(host = hostname,
                                            user = username,
                                            passwd = password,
                                            database = datab, )
        my_cursor = connection.cursor()
        print("connected")
        my_cursor.execute(query)
        print("query ausgeführt")

        if my_cursor.lastrowid:
            print('last insert id', my_cursor.lastrowid)
        else:
            print('no last insert id')
            
        connection.commit()
                        
        print("success")
        my_cursor.close()


    except mysql.connector.Error as error:
        print("failed".format(error))
    
    finally:
        if connection.is_connected():
            connection.close()