from functools import wraps
from flask import request, redirect, url_for, session


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" not in session and "username" not in session:
            return redirect(url_for("login.main", next=request.url))
        return f(*args, **kwargs)

    return decorated_function


def admin_required(func):
    """
    Modified login_required decorator to restrict access to admin group.
    """

    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_user.group != 0:        # zero means admin, one and up are other groups
            flash("You don't have permission to access this resource.", "warning")
            return redirect(url_for("main.home"))
        return func(*args, **kwargs)
    return decorated_view