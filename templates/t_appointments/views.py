import re
from unittest import TestCase
from flask import Blueprint, render_template, request,session

from helpers.decorator import login_required
from helpers.dateparse import parse
from db import insert_request, select_request, select_request_all, update_request

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
        testtype = request.form["testtype"]
        testdt = (f"{testdate} {testtime}:00")

        #username holen
        usern = session["username"]
        print("usern ",usern)

        usern_to_id = select_request(f"SELECT user_id FROM user WHERE email = '{usern}';")
        usern_to_id = usern_to_id[0]
        print("usern_to_id ",usern_to_id)
        print("testtype ",testtype)
        testtype_id = select_request(f"SELECT testtype_nr FROM test_type WHERE testmethod = '{testtype}' ")
        testtype_id = testtype_id[0]
        data.append(str(testtype_id))
        print("testtype_id ",testtype_id)
        print(f"INSERT INTO test_appoints(user_id, datetime, testtype_nr ) VALUES({usern_to_id}, '{testdt}', {testtype_id})")
        insert_request(f"INSERT INTO test_appoints(user_id, datetime, testtype_nr ) VALUES({usern_to_id}, '{testdt}', {testtype_id})")
        #update_request(f"UPDATE test_appoints SET testtype_nr = {testtype_id} WHERE ")
        print(data)
        return render_template('t_appointments.html', 
            data = data,
        )

    else:
        return render_template('t_appointments.html',
            data = data, 
        )