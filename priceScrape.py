#Live prices of Bitcoin, Ethereum and Litecoin

#*******WEBSCRAPED CRYPTOCURRECNY PRICES********

from bs4 import BeautifulSoup
import requests
from urllib2 import urlopen

import re
import time
import datetime
import csv
from csv import reader

with open('cryptPrices.csv', 'a') as csv_file:
    writer = csv.writer(csv_file, delimiter =",")
    writer.writerow(('bitPrice', 'ethPrice', 'litePrice', 'time'))

while True:
    #*****WORKS*****
    url = 'https://www.livecoinwatch.com/'

    page = requests.get(url)
    #page = urlopen(url)

    #soup = BeautifulSoup(page, 'html')

    soup = BeautifulSoup(page.text, 'html.parser')
    #soup = BeautifulSoup(page, 'lxml')
    # print soup1


    #THIS WORKS
    #x = soup.tbody.tr("td")
    #x = soup.tbody.tr("td", "nth-child(3)")
    #THIS WORKS AND ITS AMAZING
    bit = soup.tbody.find("td").next_sibling.next_sibling.next_sibling
    bitPrice = bit.get_text()
    print bit.get_text()
    #\30 > td:

    eth = soup.tbody.find("tr").next_sibling.td.next_sibling.next_sibling.next_sibling
    ethPrice = eth.get_text()
    print eth.get_text()


    #Litecoin Price Scrape
    lite = soup.tbody.find("tr").next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.td.next_sibling.next_sibling.next_sibling
    litePrice = lite.get_text()
    print lite.get_text()
        # print soup1

    with open('cryptPrices.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter =",")
                #writer.writerow((0, 0.0, 0.00))
        writer.writerow([bitPrice, ethPrice, litePrice, datetime.datetime.now()])
    

    time.sleep(10)


'''
    #RIPPLE PRICE SCRAPE
    rip = soup.tbody.find("tr").next_sibling.next_sibling.td.next_sibling.next_sibling.next_sibling
    ripPrice = rip.get_text()
    print rip.get_text()
'''
