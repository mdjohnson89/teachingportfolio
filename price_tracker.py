import json
import requests
import matplotlib.pyplot as plt


symbol = input('Which stock would you like to follow? (Enter stock symbol): ')
num_days = int(input('How many days back? : '))
API_KEY = 'WQT4AM73F83AQIO6'

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}'

response = requests.get(url)
table = response.json()

time_series_daily = table['Time Series (Daily)']

close_values = []
values = []
for key in time_series_daily:
    close_values.append(float(time_series_daily[key]['4. close']))

for i in range(num_days):
    values.append(close_values[i])

days = [x for x in range(num_days)]

print(days)
print(values)
plt.plot(days, values)
plt.show()