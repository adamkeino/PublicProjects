from flask import Blueprint, render_template, redirect, request, flash, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
# hashing function to obfuscate password and increase app 
from . import db

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
            flash('Email too short', category="error")
        elif len(firstName) < 3:
            flash('Please enter a valid first name', category="error")
        elif len(lastName) < 3:
            flash('Please enter a valid last name', category="error")
        elif password1 != password2:
            flash('Passwords do not match', category="error")
        else:
            new_user = User(email=email, first_name=firstName, 
                            last_name=lastName, 
                            password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add('new_user')
            db.session.commit()
            flash('Account created successfully', category="success")
            return redirect(url_for('views.home'))

    return render_template("signup.html")


