import json
import requests
import matplotlib.pyplot as plt

# Data from the Covid Tracking Project
url = "https://covidtracking.com/api/v1/states/daily.json"
data = json.loads(requests.get(url).text)

fig = plt.figure()
fig.set_figheight(8)
fig.set_figwidth(13)

x = []
y = []
sizes = []
labels = []

# The data for the most recent day (56 US states and Territories)
for i in range(57):
    if data[i]['death'] is None:
        continue
    if data[i]['death'] > 20000:
        # Only states with death counts exceeding 3000
        x.append(data[i]['positive'])
        y.append(data[i]['death'])
        sizes.append((data[i]['positive'] / data[i]['total']) * 8000)
        labels.append(data[i]['state'])

# Create a scatter plot
plt.scatter(x, y, s=sizes, color='red', edgecolors="black")

# Add labels
for i in range(len(labels)):
    plt.annotate(labels[i], (x[i], y[i]), ha='center', va='center')
plt.suptitle('Deaths vs. Total Confirmed Cases\n' + 'Dot Size = Relative % Positive\n' + 'States w/ 20,000+ Deaths')
plt.xlabel('Total Confirmed Cases')
plt.ylabel('Deaths')

# Show the figure
plt.show()


