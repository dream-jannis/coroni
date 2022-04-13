import email
from turtle import st
from flask import render_template, request, session, Blueprint

from db import select_request

register = Blueprint("register", __name__, template_folder="pages")

@register.route('/', methods=['POST', 'GET'])
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
        
        
        query = f"INSERT INTO vax_status(impf_count, rec_count, last_impf, last_rec) VALUES({impf_count}, {rec_count}, '{last_impf}', '{last_rec}');"
        select_request(query)


        query = f"INSERT INTO address(housenumber, street, plz, city, state, country) VALUES({housenumber}, '{street}', {plz}, '{city}', '{state}', '{country}');"
        select_request(query)

        query = f"INSERT INTO customers(surname, name, email, password, birthday) VALUES('{surname}', '{lastname}', '{mail}', '{password}', '{birthday}');"
        select_request(query)



        return render_template('register.html')

    return render_template('register.html')