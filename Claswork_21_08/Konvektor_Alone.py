import requests
import json


result = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5')
obj = json.loads(result.content)
try:

    currency = input("Enter your currency :: EUR or USD :: ")
    if not(currency == 'EUR' or currency == 'USD'):
        raise Exception

    currency_choose = 0

    if currency == 'EUR':
        print('buy EUR --> {}'.format(obj[0]['buy']))
        print('sale EUR --> {}'.format(obj[0]['sale']))
        
        choose = input("buy or sale UAH :: ")
        if not(choose == 'buy' or choose == 'sale'):
            raise Exception
        if choose == 'buy':
            currency_choose = obj[0]['buy']
        elif choose == 'sale':
            currency_choose = obj[0]['sale']
    elif currency == 'USD':
        print('buy EUR --> {}'.format(obj[1]['buy']))
        print('sale EUR --> {}'.format(obj[1]['sale']))
        
        choose = input("buy or sale UAH :: ")
        if not(choose == 'buy' or choose == 'sale'):
            raise Exception
        if choose == 'buy':
            currency_choose = obj[1]['buy']
        elif choose == 'sale':
            currency_choose = obj[1]['sale']

    amount = float(input("Enter amount: "))
    result = amount * float(currency_choose)

    print("UAN :: ", result)
except Exception:
        print("Incorrect name entered")

 
    