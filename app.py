from flask import Flask, redirect, url_for

from templates.index.views import index
from templates.login.views import login
from templates.register.views import register
from templates.profil.views import profil
from templates.impf_appointments.views import impf_appointments
from templates.t_appointments.views import t_appointments
from templates.admin.views import admin
from templates.smiley.views import smiley

app = Flask(__name__)

app.config.update(dict(SECRET_KEY="%ptsdwkf§$&%23rj43§$§kfev3it9cu9w$"))

app.register_blueprint(index, url_prefix="/")
app.register_blueprint(login, url_prefix="/login")
app.register_blueprint(register, url_prefix="/register")
app.register_blueprint(profil, url_prefix="/profil")
app.register_blueprint(impf_appointments, url_prefix="/impf_appointments")
app.register_blueprint(t_appointments, url_prefix="/t_appointments")
app.register_blueprint(admin, url_prefix="/admin")
app.register_blueprint(smiley, url_prefix="/smiley")

@app.errorhandler(Exception)
def server_error(err):
    return redirect(url_for("index.main"))

if __name__ == "__main__":
    app.run('localhost', debug=True, use_reloader=True)