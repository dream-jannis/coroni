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
    #username holen
    def get_test():

        timestamp = select_request_all(f"SELECT datetime FROM test_appoints WHERE user_id='{session['id']}';")
        result = select_request_all(f"SELECT result FROM test_appoints WHERE user_id='{session['id']}';")
        testtypenr = select_request_all(f"SELECT testtype_nr FROM test_appoints WHERE user_id='{session['id']}';")    

        data = []
        empty_list = []
        i = 0

        for row in timestamp:
            timestamprow = parse(row)
            empty_list.append(str(timestamprow))
            tstnr = str(testtypenr[i])
            tstnr = tstnr.replace("(","")
            tstnr = tstnr.replace(")","")
            tstnr = tstnr.replace(",","")
            if tstnr == "1":
                tstnr = "Schnelltest"
            elif tstnr == "2":
                tstnr = "PCR-Test"
            elif tstnr == "3": 
                tstnr = "AntiGen-Test"
            empty_list.append(tstnr)

            rslt = str(result[i])
            rslt = rslt.replace("(","")
            rslt = rslt.replace(")","")
            rslt = rslt.replace(",","")
            if rslt == "None":
                rslt = "Ergebnis noch nicht verfügbar"
            empty_list.append(rslt)

            data.append(empty_list)
            empty_list = []
            i = i + 1

        return data
    
    data = get_test()
    is_admin = session["admin_logged_in"]
    
    if request.method == "POST":
        #Daten in DB eintragen
        testdate = request.form["date"]
        testtime = request.form["time"]
        testtype = request.form["testtype"]
        testdt = (f"{testdate} {testtime}:00")

    
        testtype_id = select_request(f"SELECT testtype_nr FROM test_type WHERE testmethod = '{testtype}' ")
        testtype_id = testtype_id[0]
        
        insert_request(f"INSERT INTO test_appoints(user_id, datetime, testtype_nr ) VALUES({session['id']}, '{testdt}', {testtype_id})")
        #update_request(f"UPDATE test_appoints SET testtype_nr = {testtype_id} WHERE ")
        data = get_test()
        return render_template('t_appointments.html', 
            data = data,
            is_admin = is_admin
        )

    else:
        return render_template('t_appointments.html',
            data = data,
            is_admin = is_admin
        )