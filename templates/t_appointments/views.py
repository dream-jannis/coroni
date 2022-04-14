import re
from unittest import TestCase
from flask import Blueprint, render_template, request,session

from helpers.decorator import login_required
from helpers.dateparse import parse
from db import insert_request, select_request, select_request_all

t_appointments = Blueprint("t_appointments", __name__, template_folder="pages")

@t_appointments.route('/', methods=("POST","GET"))
@login_required
def main():
    #Daten aus DB abfragen
    timestamp = select_request_all("SELECT datetime FROM test_appoints")#WHERE userid == session iwie sowas
    result = select_request_all("SELECT result FROM test_appoints")
   

    data = []
    i = 0

    for row in timestamp:
        timestamprow = parse(row)
        data.append(str(timestamprow))
        data.append(str(result[i]))
        i = i + 1
    

    if request.method == "POST":
        #Daten in DB eintragen
        testdate = request.form["date"]
        testtime = request.form["time"]
        testdt = (f"{testdate} {testtime}:00")

        #username holen
        usern = session["username"]  

        print(usern)
        usern_to_id = select_request(f"SELECT customer_id FROM customers WHERE email = '{usern}';")
        usern_to_id = usern_to_id[0]
        print(usern_to_id)

        insert_request(f"INSERT INTO test_appoints(customer_id, datetime) VALUES('{usern_to_id}', '{testdt}')")
    
        return render_template('t_appointments.html', 
            data = data,
        )

    else:
        return render_template('t_appointments.html',
            data = data, 
        )