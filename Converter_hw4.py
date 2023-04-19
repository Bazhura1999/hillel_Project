from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/", methods=['GET' , 'POST'])
def login_user():
    if request.method == 'GET':
        pass
    else:
        pass
    return "<p>Login!</p>"

@app.route("/logout", methods=['GET'])
def logout_user():
    return "<p>Logout!</p>"

@app.route("/register", methods=['GET', 'POST'])
def register_user():
    return "Form registration"

@app.route("/user_page", methods=['GET'])
def user_access():
    return "functions"

@app.route("/currency", methods=['GET', 'POST'])
def conventer():
    return "Currency"