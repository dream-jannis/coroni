from flask import Blueprint, render_template, request, session, redirect, url_for

from helpers.decorator import login_required

smiley = Blueprint("smiley", __name__, template_folder="pages")

@smiley.route('')
@login_required
def main():
    is_admin = session["admin_logged_in"]
    return render_template('smiley.html',
        is_admin = is_admin
    )