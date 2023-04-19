from flask import Flask, request
import random
import time
from utils import get_currency_exchange_rate, get_pb_exchange_rate

app = Flask(__name__)


def random_password(name, age):
    if len(age) > 9:
        password = random.randint(10, 99)
    elif len(age) > 100:
        password = random.randint(100, 999)
    else:
        password = random.randint(1, 9)

    print(f'Привіт, {name}! Твій пароль: {password}')




@app.route("/")
def hello_world():
    return "<p><b>Hello, World!</b></p>"


@app.route("/rates", methods=['GET'])
def get_rates():
    currency_a = request.args.get('currency_a', default='USD')
    currency_b = request.args.get('currency_b', default='UAH')
    result = get_currency_exchange_rate(currency_a, currency_b)
    return result


@app.route("/rates_pb", methods=['GET'])
def get_pb_rates():
    convert_currency = request.args.get('convert_currency', default='USD')
    bank = request.args.get('bank', default='NBU') # TODO додати функцію валідації вводу банку
    if bank in ['NBU', 'nbu', 'PB', 'pb', 'PrivatBank', 'Privatbank']:
        rate_date = request.args.get('rate_date', default='01.11.2022')
        if len(rate_date) == 10:
            try:
                valid_date = time.strptime(rate_date, '%d-%m-%Y')
                result = get_pb_exchange_rate(convert_currency, bank, rate_date)
                return result
            except ValueError:
                print('Невірний формат дати!')
        elif len(rate_date) == 8:
            try:
                valid_date = time.strptime(rate_date, '%d%m%Y')
                result = get_pb_exchange_rate(convert_currency, bank, rate_date)
                return result
            except ValueError:
                print('Невірний формат дати!')
        else:
            print('Невірний формат дати!')
    else:
        print("Назва банку введена некоректно")
