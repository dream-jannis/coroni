from unittest import TestCase
from flask import Blueprint, render_template, request,session

from helpers.decorator import admin_required
from helpers.dateparse import parse
from db import insert_request, select_request, select_request_all, update_request

admin = Blueprint("admin", __name__, template_folder="pages")

@admin.route('/users', methods=("POST","GET"))
@admin_required
def main():
    is_admin = session["admin_logged_in"]
    query = f"SELECT * FROM user LEFT JOIN address ON user.address_id = address.address_id LEFT JOIN vax_status ON user.status_id = vax_status.status_id;"
    data = select_request_all(query)
    print(type(data))
    print(data)
    
    return render_template("admin.html", 
        data=data,
        is_admin = is_admin
    )

@admin.route('/appointments', methods=("POST","GET"))
@admin_required
def appointments():
    is_admin = session["admin_logged_in"]
    query = f"SELECT * FROM user LEFT JOIN address ON user.address_id = address.address_id LEFT JOIN vax_status ON user.status_id = vax_status.status_id;"
    data = select_request_all(query)
    print(type(data))
    print(data)
    
    return render_template("admin.html", 
        data=data,
        is_admin = is_admin
    )
