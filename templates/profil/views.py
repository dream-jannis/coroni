from flask import Blueprint, render_template, request, session, redirect, url_for

from helpers.decorator import login_required

profil = Blueprint("profil", __name__, template_folder="pages")

@profil.route('')
@login_required
def main():
    is_admin = session["admin_logged_in"]
    data = session["username"]
    return render_template('profil.html',
        is_admin = is_admin,
        data = data
    )

