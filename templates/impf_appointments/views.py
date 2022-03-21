from flask import Blueprint, render_template, request, session, redirect, url_for

from helpers.decorator import login_required

impf_appointments = Blueprint("impf_appointments", __name__, template_folder="pages")

@impf_appointments.route('')
@login_required
def main():
    return render_template('impf_appointments.html')

