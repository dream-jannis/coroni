from functools import wraps
from flask import request, redirect, url_for, session


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" not in session and "username" not in session:
            return redirect(url_for("login.main", next=request.url))
        return f(*args, **kwargs)

    return decorated_function


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print(session["admin_logged_in"])
        print(type(session["admin_logged_in"]))
        print(session["logged_in"] )
        print(session["username"] )
        if "logged_in" not in session and "username" not in session and session["admin_logged_in"] == False:
            return redirect(url_for("login.main", next=request.url))
        return f(*args, **kwargs)

    return decorated_function