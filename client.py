from datetime import datetime
import socket 
from bs4 import BeautifulSoup
import requests

import time

def createMessage(unique_id, price):
    url = 'https://finance.yahoo.com/quote/' + price.replace('/', '') + '%3DX'
    headers = {"User-Agent":"Mozilla/5.0"}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'lxml')
    current_time = datetime.utcnow().strftime('%d-%M-%Y %H:%M:%S:%f')[:-3]
    bid = soup.find('td', {'data-test':'BID-value'}).text
    ask = soup.find('td', {'data-test':'ASK-value'}).text
    price_feed =  ",".join([str(unique_id), price, bid, ask, current_time])
    print(price_feed)
    return price_feed

def sendMessages(s):
    prices_list = ['EUR/USD', 'EUR/GBP', 'EUR/JPY', 'EUR/CHF', 'GBP/USD', 'USD/CNY']
    unique_id = 0
    
    while True:
        for p in prices_list:           

            s.send(createMessage(unique_id, p).encode('utf8'))

            unique_id = unique_id + 1
            time.sleep(random.random())
            
            
if __name__ == '__main__':
    s = socket.socket()
    host = socket.gethostname()
    port = 9000
    s.connect((host,port))

    sendMessages(s)
