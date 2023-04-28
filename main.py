from flask import Flask, render_template, request, redirect, url_for

import requests
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt


app = Flask(__name__)


url = 'https://www.timeanddate.com/weather/?low=5'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
temps = []
temperatures = soup.find_all('td', {'class': 'rbi'})
for temp in temperatures:
    temp = temp.text.replace('°F', '')  # remove the degree symbol
    temps.append(float(temp))

x = np.arange(len(temps)) # create an array of x values
y = np.array(temps) # create an array of y values

plt.scatter(x, y) # create a scatter plot
plt.xlabel('Temperature Index') # add x-axis label
plt.ylabel('Temperature (°F)') # add y-axis label
plt.show() # show the plot

plt.hist(temps, bins=10)
plt.xlabel('Temperature (°F)')
plt.ylabel('Frequency')
plt.show()


plt.boxplot(temps)
plt.ylabel('Temperature (°F)')
plt.show()











@app.route('/')
def home():
    return render_template('index.html')





if __name__ == '__main__':
    app.run(debug=True)
