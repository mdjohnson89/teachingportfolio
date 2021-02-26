import matplotlib.pyplot as plt
import requests
import numpy as np

plt.style.use('fivethirtyeight')
r = requests.get('https://api.coindesk.com/v1/bpi/historical/close.json')
data = r.json()

p_history = data['bpi']

prices = []

for key in p_history:
    #date.append(key)
    prices.append(p_history.get(key))
date = np.arange(len(p_history))

plt.xlabel('Days Ago')
plt.ylabel('BTC Price')
plt.tight_layout()

plt.plot(date, prices)
plt.show()