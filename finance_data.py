import requests
import os

def get_currency_exchange_rate(from_currency, to_currency):
    api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    return data['Realtime Currency Exchange Rate']['5. Exchange Rate']

def get_stock_prices(symbols):
    api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
    stock_prices = {}
    for symbol in symbols:
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={api_key}'
        response = requests.get(url)
        data = response.json()
        time_series = data['Time Series (1min)']
        latest_time = sorted(time_series.keys())[0]
        stock_prices[symbol] = time_series[latest_time]['1. open']
    return stock_prices