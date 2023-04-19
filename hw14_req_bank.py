import requests
import datetime
from sqlalchemy.orm import Session
import al_db
import models_db

def get_PrivatBank_data():
    current_date = datetime.datetime.now().strftime("%d.%m.%Y")
    db_date = datetime.datetime.now().strftime("%Y-%m-%d")
    r = requests.get(f'https://api.privatbank.ua/p24api/exchange_rates?json&date={current_date}')

    currency_info = r.json()

    saleRate_USD = 0
    purchaseRate_USD = 0
    with Session(al_db.engine) as session:
        for c in currency_info['exchangeRate']:
            if c['currency'] == 'USD':
                saleRate_USD = c['saleRate']
                purchaseRate_USD = c['purchaseRate']
                purchaseRate_UAH = 1 / c['saleRate']
                saleRate_UAH = 1 / c['purchaseRate']
                UAH = c['baseCurrency']
                record1 = models_db.Currency(
                    bank='PrivatBank',
                    currency=UAH,
                    date_exchange=db_date,
                    buy_rate=purchaseRate_UAH,
                    sale_rate=saleRate_UAH
                )
                session.add(record1)
                session.commit()


    with Session(al_db.engine) as session:
        for c in currency_info['exchangeRate']:
            currency_name = c['currency']
            if c.get('saleRate'):
                print(c)
                saleRate_currency = c['saleRate'] / saleRate_USD
                purchaseRate_currency = c['purchaseRate'] / purchaseRate_USD
                record = models_db.Currency(
                    bank='PrivatBank',
                    currency=currency_name,
                    date_exchange=db_date,
                    buy_rate=purchaseRate_currency,
                    sale_rate=saleRate_currency
                )
                session.add(record)
                session.commit()

get_PrivatBank_data()