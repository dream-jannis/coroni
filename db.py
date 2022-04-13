from logging import root
import mysql.connector


from coronisecrets import hostname, username, password, datab




def connect(self):
    self.my_db = mysql.connector.connect(host = hostname,
        user = username,
        passwd = password,
        database = datab, )


def select_request(query, self):
    my_cursor = self.mydb.cursor()
    my_cursor.execute(query)
    row = my_cursor.fetchone()

    self.mydb.commit()

    return row

def disconnect(self):   
    self.mydb.close()
    



"""

"""