#This is v1 of SU_21 VIX Project $Automate$
from flask import Flask, request
import requests
from prettytable import PrettyTable

# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     api_key = 'fa2186b8-20ab-4297-a3c2-4d9a4ff32387'
#     api_endpoint = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY='
#     r = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY=' + 'api_key')
#     json_data = r.json()
#     cryptodata = json_data['data']
#     json_data = requests.get(api_endpoint).json()
#     for currency in cryptodata:
#         curr_name = currency['name']
#         curr_price = currency['quote']['USD']['price']
#         curr_change_1h = currency['quote']['USD']['percent_change_1h']
#         curr_change_24h = currency['quote']['USD']['percent_change_24h']
#         curr_change_7d = currency['quote']['USD']['percent_change_7d']
#         tableobj.add_row([curr_name, curr_price, curr_change_1h, curr_change_24h, curr_change_7d])
#
#         tableobj.field_names = ['Currency Name', 'Currency Price', 'Currency 1h Change', 'Currency 24h Change',
#                             'Currency 7d Change']
#
#         return tableobj
#
#
# if __name__ == "__main__":
#     app.run(debug=True)
