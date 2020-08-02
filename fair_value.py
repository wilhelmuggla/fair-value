import requests
from bs4 import BeautifulSoup
from pprint import pprint
import datetime
import json
import os
import sys
from colorama import Fore, Style

#read portfolio value from portfolio.json
with open(os.path.join(sys.path[0], 'portfolio.json'), "r") as f:
  portfolio = json.load(f)

#sets date
now = datetime.datetime.now()

#overall portfolio value
portfolio_value = 0


print(f"\n\n{Fore.RED}Fair value calculation - " + now.strftime("%Y-%m-%d %H:%M") +  f" {Style.RESET_ALL}\n")

for crypto in portfolio:
    #getting the page
    page = requests.get(crypto['url'])

    #parsing the page
    soup = BeautifulSoup(page.content, 'html.parser')

    #finding the price
    price = soup.find("p", {"class": "text-25px"}).get_text().strip()

    #removing text from price
    price = price.split(' ')[0]

    #converting price to float
    price = float(price)

    value = price * crypto['amount']

    #updating portfolio value
    portfolio_value += value  

    print(crypto['crypto'] + " " + str(crypto['amount']) + " * " + str(price) + " = " + str(round(value, 2)) + "kr")

#rounds portfolio value
portfolio_value = round(portfolio_value, 2)

#print portfolio value
print(f"\nPortfolio Value: \033[4m" + str(portfolio_value) + f"\033[0mkr\n\n")
