from flask import Blueprint, render_template, request, session, redirect, url_for

from helpers.decorator import login_required

profil = Blueprint("profil", __name__, template_folder="pages")

@profil.route('')
@login_required
def main():
    return render_template('profil.html')

