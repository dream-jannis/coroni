from logging import root
import mysql.connector


from coronisecrets import hostname, username, password, datab

#SELECT ONE ROW OF DATA
def select_request(query):
    try:
        connection = mysql.connector.connect(host = hostname,
                                            user = username,
                                            passwd = password,
                                            database = datab, )
        my_cursor = connection.cursor()
        my_cursor.execute(query)
        row = my_cursor.fetchone()
        output = row
                
        my_cursor.close()

        return output

    except mysql.connector.Error as error:
        print("select request failed".format(error))
    
    finally:
        if connection.is_connected():
            connection.close()



#INSERT DATA IN TABLE
def insert_request(query):
    try:
        connection = mysql.connector.connect(host = hostname,
                                            user = username,
                                            passwd = password,
                                            database = datab, )
        my_cursor = connection.cursor()
        my_cursor.execute(query)

        if my_cursor.lastrowid:
            print('last insert id', my_cursor.lastrowid)
        else:
            print('no last insert id')
            
        connection.commit()
                        
        my_cursor.close()


    except mysql.connector.Error as error:
        print("insert failed".format(error))
    
    finally:
        if connection.is_connected():
            connection.close()



#SELECT ALL VALUES THAT HIT
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
        print("all select failed".format(error))
    
    finally:
        if connection.is_connected():
            connection.close()


#UPDATE TABLE
def update_request(query):
    try:
        connection = mysql.connector.connect(host = hostname,
                                            user = username,
                                            passwd = password,
                                            database = datab, )
        my_cursor = connection.cursor()
        my_cursor.execute(query)
        connection.commit()

    
    except mysql.connector.Error as error:
        print("update failed".format(error))
    
    finally:
        if connection.is_connected():
            connection.close()