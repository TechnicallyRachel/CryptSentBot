#master file that runs everything
#ALL OTHER FILES ARE SNIPPETS INCLUDED HERE

#analyse data from bitcoin, litecoin and ethereum
import tweepy, time
from twython import Twython, TwythonError
from textblob import TextBlob #about textblob accuracy https://stackoverflow.com/questions/34518570/how-are-sentiment-analysis-computed-in-blob
import csv
from csv import reader
import datetime
from credentials import * #keys to twitter app in this file
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pylab import figure
import numpy as np
from numpy import genfromtxt
import pandas as pd

from threading import Thread
import os

from bs4 import BeautifulSoup
import requests
from urllib2 import urlopen

import re



#*****Write initial SENTIMENT CSVs*****
#(to be deleted) outside 1 hr loop to get just 1 header
# If inside loop - will write header for each tweet
#Will not average properly

with open('cryptData.csv', 'a') as csv_file:
    writer = csv.writer(csv_file, delimiter =",")
    writer.writerow(('avBitPol', 'avLitePol', 'avEthPol', 'bitPrice', 'ethPrice', 'litePrice', 'time'))


def start1st():
    while True:
        #*****WEB SCRAPE LIVE PRICES*****
        url = 'https://www.livecoinwatch.com/'

        page = requests.get(url)
        #page = urlopen(url)
        #soup = BeautifulSoup(page, 'html')
        #soup = BeautifulSoup(page, 'lxml')
        soup = BeautifulSoup(page.text, 'html.parser')

        #THIS WORKS
        #x = soup.tbody.tr("td")
        #x = soup.tbody.tr("td", "nth-child(3)")
        #(THIS IS BETTER)

        #Bitcoin Price Scrape
        bit = soup.tbody.find("td").next_sibling.next_sibling.next_sibling
        bitPrice = bit.get_text()
        print bit.get_text()
        
        #Ethereum Price Scrape 
        eth = soup.tbody.find("tr").next_sibling.td.next_sibling.next_sibling.next_sibling
        ethPrice = eth.get_text()
        print eth.get_text()

        #Litecoin Price Scrape
        lite = soup.tbody.find("tr").next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.td.next_sibling.next_sibling.next_sibling
        litePrice = lite.get_text()
        print lite.get_text()

        """
        with open('cryptPrices.csv', 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter =",")
                    #writer.writerow((0, 0.0, 0.00))
            writer.writerow([bitPrice, ethPrice, litePrice, datetime.datetime.now()])
        """
        '''
        #Did not use Ripple because of possible word meaning interfeirance of analysis
            #RIPPLE PRICE SCRAPE
            rip = soup.tbody.find("tr").next_sibling.next_sibling.td.next_sibling.next_sibling.next_sibling
            ripPrice = rip.get_text()
            print rip.get_text()
        '''

        
        #*****WRITE ALL TEMP CSV FILES TO BE AVERAGED***
        
        with open('bitDataTemp.csv', 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter =",")
            writer.writerow(('Pol', 'Sub', 'time'))

        with open('liteDataTemp.csv', 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter =",")
            writer.writerow(('Pol', 'Sub', 'time'))

        
        with open('ethDataTemp.csv', 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter =",")
            writer.writerow(('Pol', 'Sub', 'time'))
            
        """
        #DO NOT USE MASTER TEMP FILE - SCREWS UP FLOW
         with open('cryptDataTemp.csv', 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter =",")
            writer.writerow(('bitPol', 'bitSub', 'litePol', 'liteSub', 'ethPol', 'ethSub','time'))                           
        """
        
        #******RETREIVING TWEETS FOR ANALYSIS****
        #This logs us in to twitter using the tweepy library
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

        api = tweepy.API(auth)

        #Retrieve Tweets

        bitcoin_tweets = api.search('bitcoin', count=10)
        litecoin_tweets = api.search('litecoin', count=10)
        ethereum_tweets = api.search('ethereum', count=10)

            #public_tweets = api.search(" -RT", 'bitcoin', count=10)


    #**********BITCOIN PORTION****************
        for tweet in bitcoin_tweets:
            
            #tweet.lang == "en"
    #        print(tweet.text)
                
            #Perform Sentiment Analysis on Tweets
            analysis = TextBlob(tweet.text)
            # data.append http://altitudelabs.com/blog/web-scraping-with-python-and-beautiful-soup/
            
            #WRITING CSV FILE 1 - THIS CSV WILL NEED TO WRITE OVER ITSELF
            #(Make sure this is within the "for tweet" for loop to save each tweet info correctly)
            with open('bitDataTemp.csv', 'a') as csv_file: #a = append MUST STAY 'a'
                # TextBlob parsing info: http://textblob.readthedocs.io/en/dev/quickstart.html#sentiment-analysis
                writer = csv.writer(csv_file, delimiter =",")
                writer.writerow([analysis.sentiment.polarity,
                    analysis.sentiment.subjectivity, datetime.datetime.now()])

    #***************LITECOIN PORTION*****************
        for tweet in litecoin_tweets:
            
            #tweet.lang == "en"
    #        print(tweet.text)
                
            #Perform Sentiment Analysis on Tweets
            analysis = TextBlob(tweet.text)

            #WRITING TEMP CSV- THIS CSV WILL NEED TO WRITE OVER ITSELF
            #(Make sure this is within the "for tweet" for loop to save each tweet info correctly)
            with open('liteDataTemp.csv', 'a') as csv_file: #a = append MUST STAY 'a'
                # TextBlob parsing info: http://textblob.readthedocs.io/en/dev/quickstart.html#sentiment-analysis
                writer = csv.writer(csv_file, delimiter =",")
                writer.writerow([analysis.sentiment.polarity,
                    analysis.sentiment.subjectivity, datetime.datetime.now()])

    #****************ETHEREUM PORTION****************

        for tweet in ethereum_tweets:
            #tweet.lang == "en"
    #        print(tweet.text)
                
            #Perform Sentiment Analysis on Tweets
            analysis = TextBlob(tweet.text)
            # data.append http://altitudelabs.com/blog/web-scraping-with-python-and-beautiful-soup/
            
            #WRITING TEMP CSV FILE - THIS CSV WILL NEED TO WRITE OVER ITSELF
            #(Make sure this is within the "for tweet" for loop to save each tweet info correctly)
            #insert for loop here?

            with open('ethDataTemp.csv', 'a') as csv_file: #a = append MUST STAY 'a'
                # TextBlob parsing info: http://textblob.readthedocs.io/en/dev/quickstart.html#sentiment-analysis
                writer = csv.writer(csv_file, delimiter =",")
                writer.writerow([analysis.sentiment.polarity,
                    analysis.sentiment.subjectivity, datetime.datetime.now()])


    #***WRITING FROM TEMPS TO SINGLE HOURLY CSV*******
        #Extract [Pol] as numbered list variable using Pandas
        bitdata = pd.read_csv("bitDataTemp.csv", sep = ",")
        bitPol = bitdata['Pol']
        #Sub = data["0.0"]
                    
        #FIND THE AVERAGE POL AND SUB
        #THIS ALL WORKS - FROM NUMPY
        findBitPol = np.array([bitPol]).astype(np.float)
        avBitPol = np.mean(findBitPol, dtype=np.float64)

        litedata = pd.read_csv("liteDataTemp.csv", sep = ",")
        litePol = litedata['Pol']
                    
        findLitePol = np.array([litePol]).astype(np.float)
        avLitePol = np.mean(findLitePol, dtype=np.float64)

        ethdata = pd.read_csv("ethDataTemp.csv", sep = ",")
        ethPol = ethdata['Pol']
                    
        findEthPol = np.array([ethPol]).astype(np.float)
        avEthPol = np.mean(findEthPol, dtype=np.float64)

        #*****WRITE SINGLE PERMANENT CSV***
        with open('cryptData.csv', 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter =",")
                    #writer.writerow((0, 0.0, 0.00))
            writer.writerow([avBitPol, bitPrice, avLitePol, litePrice, avEthPol, ethPrice, datetime.datetime.now()])

    #*********DELETE TEMP CSV FILES TO BE RE-WRITTEN**********
            
            #DELETE 1st temp CSV file - the one with tweets to be averaged.
        os.remove('bitDataTemp.csv')
        os.remove('liteDataTemp.csv')
        os.remove('ethDataTemp.csv')
        
        #Executes every 30 seconds 
        time.sleep(30)

