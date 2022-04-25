from datetime import datetime

from bs4 import BeautifulSoup
import requests
def createMessage(fx):
    url = 'https://finance.yahoo.com/quote/' + fx.replace('/', '') + '%3DX'
    headers = {"User-Agent":"Mozilla/5.0"}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'lxml')
    current_time = datetime.utcnow().strftime('%d-%M-%Y %H:%M:%S:%f')[:-3]
    bid = soup.find('td', {'data-test':'BID-value'}).text
    ask = soup.find('td', {'data-test':'ASK-value'}).text
    price_feed =  ",".join([fx, bid, ask, current_time])
    print(price_feed)
    return price_feed
      
if __name__ == '__main__':
    fx = 'EUR/USD'
    createMessage(fx)
      