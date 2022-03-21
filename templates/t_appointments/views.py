from flask import Blueprint, render_template, request, session, redirect, url_for

from helpers.decorator import login_required

t_appointments = Blueprint("t_appointments", __name__, template_folder="pages")

@t_appointments.route('')
@login_required
def main():
    return render_template('t_appointments.html')