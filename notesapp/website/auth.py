from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('logout')
def logout():
    return "<p>Logout</p>"

@auth.route('signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email too short')
    return render_template("signup.html")


