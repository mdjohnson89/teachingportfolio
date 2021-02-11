import requests

r = requests.get('https://api.coindesk.com/v1/bpi/historical/close.json')

r.json()


