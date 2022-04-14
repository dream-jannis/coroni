from flask import Blueprint, render_template, request, session, redirect, url_for

from helpers.decorator import login_required
from db import insert_request, select_request

impf_appointments = Blueprint("impf_appointments", __name__, template_folder="pages")

@impf_appointments.route('/', methods=['POST', 'GET'])
@login_required
def main():
    if request.method == "POST":

        impfdate = request.form["date"]
        impftime = request.form["time"]
        #usern = request.form["username"]  #try getting username to get customer_id 
        impfdt = (f"{impfdate} {impftime}:00")
        usern = session["username"]  

        print(usern)
        usern_to_id = select_request(f"SELECT customer_id FROM customers WHERE email = '{usern}';")
        usern_to_id = usern_to_id[0]
        print(usern_to_id)
        insert_request(f"INSERT INTO vax_appoints(customer_id, datetime) VALUES('{usern_to_id}','{impfdt}')")
        return render_template('impf_appointments.html')


    return render_template('impf_appointments.html') 

