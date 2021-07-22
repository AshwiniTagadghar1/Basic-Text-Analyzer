from flask import Blueprint, render_template,flash
#from werkzeug.wrappers import request
#from werkzeug.utils import secure_filename

auth = Blueprint('auth', __name__)

@auth.route('/home')
def home1():
    return render_template("home.html", text="testing", len="10")  

@auth.route('/login', methods=['GET','POST'])
def login():
    return render_template("login.html", text="testing", len="10")

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    flash("email needs to have more than 4 char")
    return render_template("sign-up.html")


	

