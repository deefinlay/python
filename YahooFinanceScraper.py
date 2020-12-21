# Simple Scraper using BeautifulSoup
# Scrapes the Yahoo Finance to match a valid input stock symbol
# Returns the current stock price for that symbol

import bs4
import requests
from bs4 import BeautifulSoup

# Set up variables
readInStock = input('Enter a valid stock symbol : ')
stock = readInStock.upper()
url = f'https://uk.finance.yahoo.com/quote/{stock}'
r = requests.get(url)
web_content = bs4.BeautifulSoup(r.text,'lxml')

# Grab the stock's trading name
def parseTradingName() :
    tradingName = web_content.find_all('h1',{'class':'D(ib) Fz(18px)'})[0].text
    return tradingName

# Grab the stock's current price
def parsePrice() :
    price = web_content.find_all('span',{'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'})[0].text
    return price

# Print the stock's price to screen
def printPrice() :
    print ('Current Price for ' + parseTradingName() + ' is *** ' + str(parsePrice()), end=' GBP *** ')

while True :
    printPrice()
    refresh = input ('Enter y to refresh or anything else to exit: ')
    if refresh.lower() != 'y' :
        break
