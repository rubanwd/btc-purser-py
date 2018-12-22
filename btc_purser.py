#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import os

def get_html():
    url = 'https://coinmarketcap.com/'
    r = requests.get(url)
    return r.text

def get_btc_price(html):
    soup = BeautifulSoup(html, 'lxml')
    t = soup.find(id="id-bitcoin").find("a", class_="price").text
    result = t.split('$')[-1]
    return result

def send_message(message):
    title = 'Now cost of BTC is:'
    os.system('notify-send "{}" "{}"'.format(title, message))

def main():
    cost = get_btc_price(get_html())
    send_message(cost)

if __name__ == '__main__':
    main()