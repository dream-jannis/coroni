from flask import Flask, redirect, render_template, session, url_for

app = Flask(__name__)

@app.route('/')
def start():
    #if:
        return render_template('index.html')
    #else: 
    #    return render_template('login.html')

@app.route('/login')
def login():

    return render_template('login.html')

@app.route('/logout')
def logout():

    return redirect(url_for('/login'))

@app.route('/register')
def register():
    return render_template('register.html')
    
if __name__ == "__main__":
    app.run('localhost', debug=True, use_reloader=True)