from turtle import update
from flask import Blueprint, render_template, request, session, redirect, url_for

from helpers.decorator import login_required
from db import insert_request, select_request, update_request

profil = Blueprint("profil", __name__, template_folder="pages")

@profil.route('', methods=("POST","GET"))
@login_required
def main():
    
    is_admin = session["admin_logged_in"]
    
    def get_data():
        query = f"SELECT * FROM user LEFT JOIN address ON user.address_id = address.address_id LEFT JOIN vax_status ON user.status_id = vax_status.status_id WHERE user.email = '{session['username']}';"
        data = select_request(query)
        return data
    
    data = get_data()

    if request.method == 'POST':

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

        query = f"UPDATE user SET surname = '{surname}', name = '{lastname}', email = '{mail}', password = '{password}', birthday = '{birthday}' WHERE user_id={session['id']}"
        update_request(query)

        data = get_data()

        return render_template('profil.html',
        is_admin = is_admin,
        data = data
        )



    return render_template('profil.html',
        is_admin = is_admin,
        data = data
    )

