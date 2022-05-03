from unittest import TestCase
from flask import Blueprint, render_template, request,session

from helpers.decorator import login_required
from helpers.dateparse import parse
from db import insert_request, select_request, select_request_all, update_request

admin = Blueprint("admin", __name__, template_folder="pages")

@admin.route('/', methods=("POST","GET"))
@login_required
def main():
    all_users = select_request_all("SELECT * FROM customers LEFT JOIN address ON customers.address_id = address.address_id LEFT JOIN vax_status ON customers.status_id = vax_status.status_id")
    print(type(all_users))
    print(all_users[0][5])
    #test = parse(all_users[0][5])
    #print(test)

    data = []
    data.append(all_users)
    #print("Data: ",data,"\n")
    print("Data 0 ",data[0],"\n")
    #print("Data 0 0 ",data[0][0],"\n")
 
        
    return render_template("admin.html", data=data,)
