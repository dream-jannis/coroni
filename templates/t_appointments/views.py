from flask import Blueprint, render_template, request, session, redirect, url_for

from helpers.decorator import login_required
from db import query

t_appointments = Blueprint("t_appointments", __name__, template_folder="pages")

@t_appointments.route('/', methods=("POST","GET"))
@login_required
def main():
    if request.method == "POST":
        testdate = request.form["date"]
        testtime = request.form["time"]
        testdt = (f"{testdate} {testtime}:00")
        query(f"INSERT INTO test_appoints(datetime) VALUES({testdt})")

    return render_template('t_appointments.html')