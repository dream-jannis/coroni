import email
from turtle import st
from flask import render_template, request, session, Blueprint

from db import query

register = Blueprint("register", __name__, template_folder="pages")

@register.route('/', methods=('GET','POST'))
def main():
    if request.method == "POST":
        mail = request.form['email']
        password = request.form['password']
        surname = request.form['surname']
        lastname = request.form['name']
        birthday = request.form['birthday']
        street = request.form['street']
        housenumber = request.form['number']
        plz = request.form['plz']
        city = request.form['city']
        state = request.form['state']
        country = request.form['country']
        impf_count = request.form['anzahl_impf']
        last_impf = request.form['last_impf']
        rec_count = request.form['anzahl_rec']
        last_rec = request.form['last_rec']

        print(mail, password, surname, lastname, birthday, street, housenumber, plz, city, state, country, impf_count, last_impf, rec_count, last_rec)
        
    return render_template('register.html')