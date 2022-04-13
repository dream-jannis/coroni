from flask import Blueprint, render_template, request, session, redirect, url_for

from helpers.decorator import login_required
from db import insert_request

impf_appointments = Blueprint("impf_appointments", __name__, template_folder="pages")

@impf_appointments.route('')
@login_required
def main():
    if request.method == "POST":

        testdate = request.form["date"]
        testtime = request.form["time"]
        testdt = (f"{testdate} {testtime}:00")
        print(testdt)
        print("bis hier hin gehts")
        insert_request(f"INSERT INTO test_appoints(datetime) VALUES('{testdt}')")
        return render_template('impf_appointments.html')


    return render_template('impf_appointments.html') 

