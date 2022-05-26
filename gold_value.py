import requests
import os
import csv
from datetime import datetime as dt
from bs4 import BeautifulSoup as BS

DATE_FORMAT = '%d.%m.%Y %H:%M'
URL = "https://markets.businessinsider.com/commodities/gold-price"

def request_gold_price():
    
    r = requests.get(URL)

    soup = BS(r.text, "html.parser")
    price = soup.find('div',{'class':'price'}).string

    print(f'The current price is {price}')
    
    chars = []
    for char in price:
        if char != ',':
            chars.append(char)
    
    price = ''.join(chars)

    return price

request_gold_price()
