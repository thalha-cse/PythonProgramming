# This project is about real time currency converter which converts your amount to any other currency amount
# This project contains
# 1. forex-python library which has many facilities like currencyrates, currencysymbol, currencyname, bitcoin price of all currencies etc
# 2. from forex-python import CurrencyRates fuction
# 3. after that some variables are used to store or to fetch etc.....

from forex_python.converter import CurrencyRates
c = CurrencyRates()
# input from the user for the amount
amount = int(input("Enter the amount:- "))
# from which currency
from_currency = input("From Currency:- ").upper()
# to which currency
to_currency = input("To Currency:- ").upper()
print(from_currency, 'To', to_currency, amount)
# "convert" function converts the currency rate
result = c.convert(from_currency, to_currency, amount)
print(result)
