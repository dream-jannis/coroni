import re
from unittest import TestCase
from flask import Blueprint, render_template, request

from helpers.decorator import login_required
from helpers.dateparse import parse
from db import query

t_appointments = Blueprint("t_appointments", __name__, template_folder="pages")

@t_appointments.route('/', methods=("POST","GET"))
@login_required
def main():
    #Daten aus DB abfragen
    timestamp = query("SELECT datetime FROM test_appoints")#WHERE userid == session iwie sowas
    result = query("SELECT result FROM test_appoints")
   

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
        query(f"INSERT INTO test_appoints(datetime) VALUES('{testdt}')")
    
        return render_template('t_appointments.html', 
            data = data,
        )

    else:
        return render_template('t_appointments.html',
            data = data, 
        )