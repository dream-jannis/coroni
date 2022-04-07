from flask import Blueprint, render_template, request

from helpers.decorator import login_required
from db import query

t_appointments = Blueprint("t_appointments", __name__, template_folder="pages")

@t_appointments.route('/', methods=("POST","GET"))
@login_required
def main():
    #Daten aus DB abfragen
    timestamp = query("SELECT datetime FROM test_appoints")#WHERE userid == session iwie sowas
    #testtype = query("SELECT ")
    result = query("SELECT result FROM test_appoints")
    #timestamp = list(timestamp)
    #result = list(result)
    
    print("timestamp list: ", timestamp[0])
    print("result list: ",result)
    print(type(result))
    print(type(timestamp))
    print("das ist print timestamp ", timestamp)
    if request.method == "POST":
        #Daten in DB eintragen
        testdate = request.form["date"]
        testtime = request.form["time"]
        testdt = (f"{testdate} {testtime}:00")
        query(f"INSERT INTO test_appoints(datetime) VALUES('{testdt}')")
    
        return render_template('t_appointments.html', 
            timestamp = timestamp, 
            #testtype = testtype, 
            result = result
        )

    else:
        return render_template('t_appointments.html',
            timestamp = timestamp, 
            #testtype = testtype, 
            result = result
        )