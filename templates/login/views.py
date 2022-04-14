from flask import Blueprint, render_template, url_for, redirect, request, session
#from coronisecrets import hostname, username, password, datab
from db import select_request


login = Blueprint("login", __name__, template_folder="pages")

@login.route('/', methods=("GET","POST"))
def main():
    if (
        request.method == "POST"
        and "logged_in" not in session
        and "username" not in session
        and "admin_logged_in" not in session
        and "admin_username" not in session):
        
        usern = request.form["login"]
        user_password = request.form["password"]

        if not usern or not user_password:
            return render_template("login.html")

        query = f"SELECT email FROM customers WHERE email = '{usern}'"
        usern_req = select_request(query)

        query = f"SELECT password FROM customers WHERE password = '{user_password}'"
        passwd_req = select_request(query)

        if usern == usern_req[0]:
            if user_password == passwd_req[0]:
                session["logged_in"] = True
                session["admin_logged_in"] = True
                session["admin_username"] = usern_req
                session["username"] = usern_req
                return redirect(url_for("index.main"))
            else:
                return render_template("login.html")
        else:
            return render_template("login.html")

    else:
        if "logged_in" not in session:
            return render_template("login.html")
        else:
            return redirect(url_for("index.main"))

@login.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("login.main"))


#hardcoded login testuser
    """
    if usern == "test":
        if user_password == "test":
            session["logged_in"] = True
            session["admin_logged_in"] = True
            session["admin_username"] = "test"
            session["username"] = "test"
            return redirect(url_for("index.main"))
        else:
            return render_template("login.html")
    else:
        return render_template("login.html")
    """

