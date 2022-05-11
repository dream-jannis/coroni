from unittest import TestCase
from flask import Blueprint, render_template, request,session

from helpers.decorator import admin_required
from helpers.dateparse import parse
from db import insert_request, select_request, select_request_all, update_request

admin = Blueprint("admin", __name__, template_folder="pages")

@admin.route('/', methods=("POST","GET"))
@admin_required
def main():
    is_admin = session["admin_logged_in"]
    query = f"SELECT * FROM user LEFT JOIN address ON user.address_id = address.address_id LEFT JOIN vax_status ON user.status_id = vax_status.status_id"
    all_users = select_request_all(query)
    print(type(all_users))
    print(all_users[0][5])
    #test = parse(all_users[0][5])
    #print(test)

    data = []
    data.append(all_users)
    print("Data: ",data,"\n")
    print("Data 0 ",data[0],"\n")
    print("Data 0 0 ",data[0][0],"\n")
    #for row in all_users:
    #    data.append(str(all_users))
        
    return render_template("admin.html", 
        data=data,
        is_admin = is_admin
    )
