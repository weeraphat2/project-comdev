import email
from flask import Flask, render_template, request, flash, session
app = Flask(__name__)
app.config['SECRET_KEY'] = 'werty uiop'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['POST','GET'])
def login():
    return render_template("login.html")

@app.route('/home', methods=['POST'])
def home():
    if request.method == 'POST':
        session['email'] = request.form['email']
    return render_template("home.html")

@app.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email', None)
        return render_template("logout.html")
    else:
        return '<div class="alert alert-danger" role="alert"> A simple danger alert—check it out!</div>'

@app.route('/signup', methods=['POST','GET'])
def signup():
        return render_template("signup.html")


if __name__ == "__main__" :
    app.run(debug='true')