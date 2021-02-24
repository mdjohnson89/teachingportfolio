import matplotlib.pyplot as plt
import requests

r = requests.get('https://api.coindesk.com/v1/bpi/historical/close.json')
data = r.json()

p_history = data['bpi']

prices = []

for key in p_history:
    #date.append(key)
    prices.append(p_history.get(key))
date = [x for x in range(len(p_history))]

plt.plot(date, prices)
plt.show()