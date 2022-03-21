from flask import Blueprint, render_template, request, session, redirect, url_for

from helpers.decorator import login_required

index = Blueprint("index", __name__, template_folder="pages")

@index.route('')
@login_required
def main():
    return render_template('index.html')