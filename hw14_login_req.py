from flask import Flask
from flask import request, render_template
import al_db
import models_db
from sqlalchemy import select
from sqlalchemy.orm import Session
from flask import session as flask_session

app = Flask(__name__)
app.secret_key = 'supersecret'

@app.route("/", methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        with Session(al_db.engine) as session:
            query = select(models_db.User).filter(models_db.User.username == request.form['username'])
            result = session.execute(query).fetchall()
            if result:
                flask_session['username'] = request.form['username']
            else:
                return render_template('index.html', username='No user found')
            return render_template('index.html', username=flask_session['username'])
    else:
        return render_template('login.html')

@app.route("/logout", methods=['GET'])
def logout_user():
    #get_bank_data_task.apply_async()
    flask_session.pop('username', None)
    return "<p>Logout</p>"

@app.route("/register", methods=['GET', 'POST'])
def register_user():
    if request.method == 'GET':
        username = ['username']
        password = ['password']
        email = ['email']
        first_name = ['first_name']
        surname = ['surname']
        return render_template('register_form.html',
                               username=username,
                               password=password,
                               email=email,
                               first_name=first_name,
                               surname=surname
                               )

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        first_name = request.form['first_name']
        surname = request.form['surname']
        with Session(al_db.engine) as session:
            registration = models_db.User(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                surname=surname
            )
        session.add(registration)
        session.commit()

        return 'Регистрация прошла успешно!'