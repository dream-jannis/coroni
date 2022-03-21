from flask import render_template, session, Blueprint

register = Blueprint("register", __name__, template_folder="pages")

@register.route('/')
def main():
    return render_template('register.html')