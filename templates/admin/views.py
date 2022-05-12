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

    
    return render_template("admin.html", 
        data=data,
        is_admin = is_admin
    )

@admin.route('/appointments/impf', methods=("POST","GET"))
@admin_required
def appointments_impf():
    is_admin = session["admin_logged_in"]
    query = f"select datetime, vaccine, surname, name, email from vax_appoints JOIN user on vax_appoints.user_id=user.user_id JOIN vaccination ON vaccination.impf_id=vaccination.impf_id;"
    data = select_request_all(query)

  
    
    return render_template("appoints_impf.html", 
        data=data,
        is_admin = is_admin
    )

@admin.route('/appointments/test', methods=("POST","GET"))
@admin_required
def appointments_test():
    is_admin = session["admin_logged_in"]
    query = f"select datetime, testmethod, result, surname, name, email from test_appoints JOIN user on test_appoints.user_id=user.user_id JOIN test_type ON test_appoints.testtype_nr=test_type.testtype_nr;"
    data = select_request_all(query)

    #query = f"select datetime, testmethod, result, surname, name, email from test_appoints JOIN user on test_appoints.user_id=user.user_id JOIN test_type ON test_appoints.testtype_nr=test_type.testtype_nr WHERE result is null;"
       
    return render_template("appoints_test.html", 
        data=data,
        is_admin = is_admin
    )