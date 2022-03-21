from flask import Blueprint, render_template, url_for, redirect, request, session

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
        user = request.form["login"]
        password = request.form["password"]

        if not user or not password:
            return render_template("login.html")

        if user == "test":
            if password == "test":
                session["logged_in"] = True
                session["admin_logged_in"] = True
                session["admin_username"] = "test"
                session["username"] = "test"
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