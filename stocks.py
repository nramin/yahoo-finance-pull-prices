import urllib2
from decimal import *
from bs4 import BeautifulSoup

stocks = ['CSCO', 'MSFT', 'SBUX', 'JWN', 'DIS', 'USO']

def getChange(yesterday_price, current_price):
    change = Decimal(((float(current_price) - float(yesterday_price)) / float(yesterday_price) * 100))
    change = round(change,2)
    return change

for stock in stocks:
    stock_page = urllib2.urlopen("http://finance.yahoo.com/q?s=" + stock).read()
    soup = BeautifulSoup(stock_page)

    general_info = soup.find("div", {"id": "yfi_investing_content"})
    company_name = general_info.find("div", {"class": "title"}).find("h2")
    yesterday_price = ''
    current_price = general_info.find("span", {"class": "time_rtq_ticker"}).getText()

    print('Information for: ' + company_name.getText())

    table = soup.find("table", {"id": "table1"})

    count = 0
    for stat in table.findAll('tr'):
        if count < 2:
            if count == 0:
                yesterday_price = stat.find('td').getText()
            print(stat.find('th').getText() + " $" + stat.find('td').getText())
            count = count + 1
    print("Current: $" + current_price)
    print("Change: " + str(getChange(yesterday_price, current_price))+ "%")
    print('')
