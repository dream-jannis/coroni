from dataclasses import dataclass
import imp
from flask import Blueprint, render_template, request, session, redirect, url_for

from helpers.decorator import login_required
from helpers.dateparse import parse
from db import insert_request, select_request, select_request_all, update_request

impf_appointments = Blueprint("impf_appointments", __name__, template_folder="pages")

@impf_appointments.route('/', methods=['POST', 'GET'])
@login_required
def main():
    print("test")

    def get_impf():

        timestamp = select_request_all(f"SELECT datetime FROM vax_appoints WHERE user_id='{session['id']}';")
        impfnr = select_request_all(f"SELECT impf_id FROM vax_appoints WHERE user_id='{session['id']}';")   
        appoints_id = select_request_all(f"SELECT vax_appoints_id FROM vax_appoints WHERE user_id='{session['id']}';")  

        data = []
        empty_list = []
        i = 0

        for row in timestamp:
            timestamprow = parse(row)
            empty_list.append(str(timestamprow))
            impf = str(impfnr[i])
            impf = impf.replace("(","")
            impf = impf.replace(")","")
            impf = impf.replace(",","")
            if impf == "1":
                impf = "BioNTech"
            elif impf == "2":
                impf = "AstraZeneca"
            elif impf == "3": 
                impf = "Moderna"
            elif impf == "4":
                impf = "NovoVax"
            empty_list.append(impf)
            a_id = str(appoints_id[i])
            empty_list.append(a_id)

            data.append(empty_list)
            empty_list = []
            i = i + 1
        return data

    data = get_impf()
    is_admin = session["admin_logged_in"]

    if request.method == "POST":
        #Daten in DB eintragen
        testdate = request.form["date"]
        testtime = request.form["time"]
        vaccine = request.form["vaccine"]
        impfdt = (f"{testdate} {testtime}:00")

    
        vaccine_id = select_request(f"SELECT impf_id FROM vaccination WHERE vaccine = '{vaccine}' ")
        vaccine_id = vaccine_id[0]

        insert_request(f"INSERT INTO vax_appoints(user_id, datetime, impf_id ) VALUES({session['id']}, '{impfdt}', {vaccine_id})")
        #update_request(f"UPDATE test_appoints SET testtype_nr = {testtype_id} WHERE ")
        data = get_impf()

        return render_template('impf_appointments.html', 
            data = data,
            is_admin = is_admin
        )

    else:
        return render_template('impf_appointments.html',
            data = data,
            is_admin = is_admin
        )

@impf_appointments.route('/update/<id>/', methods=("POST","GET"))
@login_required
def update(id):    
    id = id.replace("(","").replace(")","").replace(",","")

    query = f"DELETE FROM vax_appoints WHERE vax_appoints_id={id} AND user_id={session['id']}"
    update_request(query)

    return redirect('/impf_appointments')