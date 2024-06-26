from flask import Blueprint, render_template, url_for, redirect, request, session
from db import select_request


login = Blueprint("login", __name__, template_folder="pages")

@login.route('/', methods=("GET","POST"))
def main():
    if (
        request.method == "POST"
        and "logged_in" not in session
        and "username" not in session
        and "admin_logged_in" not in session
        and "admin_username" not in session
    ):
        usern = request.form["login"]
        user_password = request.form["password"]

        query = f"SELECT email FROM user WHERE email = '{usern}'"
        usern_req = select_request(query)
        query = f"SELECT password FROM user WHERE password = '{user_password}'"
        passwd_req = select_request(query)

        query = f"SELECT is_admin FROM user WHERE email = '{usern}'"
        is_admin = select_request(query)
        is_admin = is_admin[0]

        if not usern or not user_password:
            return render_template("login.html")

        elif usern == usern_req[0]:
            if user_password == passwd_req[0]:
                session["logged_in"] = True
                session["admin_username"] = request.form["login"]
                session["username"] = request.form["login"]
                usern_to_id = select_request(f"SELECT user_id FROM user WHERE email = '{usern}';")
                usern_to_id = usern_to_id[0]
                session["id"] = usern_to_id
                if is_admin == 1:
                    session["admin_logged_in"] = True
                else:
                    session["admin_logged_in"] = False
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