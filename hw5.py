from flask import Flask
from flask import request, render_template
import sqlite3
from database_func import DBManager

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def login_user():
    if request.method == 'GET':
        pass
    else:
        pass
    return "<p>login</p>"

@app.route("/logout", methods=['GET'])
def logout_user():
    return "<p>Logout</p>"

@app.route("/register", methods=['GET', 'POST'])
def register_user():
    return("Registration form")

@app.route("/user_page", methods=['GET'])
def user_acces():
    return("More functions")

@app.route("/currency", methods=['GET', 'POST'])
def currency_converter():
    if request.method == 'POST':
        user_bank = request.form['bank']
        user_currency_1 = request.form['currency_1']
        user_date = request.form['date']
        user_currency_2 = request.form['currency_2']

        with DBManager() as db:
            buy_rate_1, sale_rate_1 = db.get_result(f'SELECT buy_rate, sale_rate FROM currency WHERE bank="{user_bank}" and date_exchange="{user_date}" and currency="{user_currency_1}"')
            buy_rate_2, sale_rate_2 = db.get_result(f'SELECT buy_rate, sale_rate FROM currency WHERE bank="{user_bank}" and date_exchange="{user_date}" and currency="{user_currency_2}"')

        cur_exchange_buy = buy_rate_2 / buy_rate_1
        cur_exchange_sale = sale_rate_2 / sale_rate_1
        return render_template('data_form.html',
                               cur_exchange_buy=cur_exchange_buy,
                               cur_exchange_sale=cur_exchange_sale,
                               user_currency_1=user_currency_1,
                               user_currency_2=user_currency_2)
    else:
        return render_template('data_form.html')