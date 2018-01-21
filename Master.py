#MASTER FILE THAT RUNS EVERYTHING
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

import threading
from threading import Thread
import os

from bs4 import BeautifulSoup
import requests
from urllib2 import urlopen

import re
from bs4 import BeautifulSoup
import requests
from urllib2 import urlopen


#*****Write initial SENTIMENT CSVs*****
#(to be deleted) outside 1 hr loop to get just 1 header
# If inside loop - will write header for each tweet
#Will not average properly

with open('cryptData.csv', 'a') as csv_file:
    writer = csv.writer(csv_file, delimiter =",")
    writer.writerow(('avBitPol', 'bitPrice', 'avLitePol', 'litePrice', 'avEthPol', 'ethPrice', 'time'))


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
        #*****WRITE MASTER PERMANENT CSV***
        with open('cryptMasterData.csv', 'a') as csv_file:
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

#*****************************start2nd.py************************************
def start2nd():
    while True:

        #********READING SENTIMENT DATA******
        #READ CSV COLUMN AS NUMBERED LIST (NOT STRING)
        """
        bitDataAv = pd.read_csv("bitData.csv", sep = ",")
        liteDataAv = pd.read_csv("liteData.csv", sep = ",")
        ethDataAv = pd.read_csv("ethData.csv", sep = ",")
        #print data.head()
        """
        dataAv = pd.read_csv("cryptData.csv", sep = ",")

        #DEFINING VARIABE TO GRAPH
        bitAvPol = dataAv["avBitPol"]
        #print bitAvPol
        liteAvPol = dataAv["avLitePol"]
        print liteAvPol
        ethAvPol = dataAv["avEthPol"]
        #print ethAvPol

        dfcall=dataAv.astype('datetime64[ns]')
        Time = dfcall["time"]
        #print Time

        #DEFINING VARIABE TO GRAPH
        bitPrice = dataAv["bitPrice"]
        #print bitPrice
        ethPrice = dataAv["ethPrice"]
        #print liteAvPol
        litePrice = dataAv["litePrice"]
        #print ethAvPol

        a1 = bitPrice
        a2 = litePrice
        a3 = ethPrice
        #print a1, a2, a3

        x = Time
        #x = [Time]
        y1 = bitAvPol
        y2 = liteAvPol
        y3 = ethAvPol

        #TAKING AVERAGE POLARITY OF THE HOUR

        # Extract [Pol] as numbered list variable using pandas
        #data = pd.read_csv("ethDataTemp.csv", sep = ",")
        #bitPol = data['Pol']
        #Sub = data["0.0"]
                    
        #FIND THE AVERAGE POL AND SUB FOR THE HOUR
            #THIS ALL WORKS - FROM NUMPY
        findBitPol = np.array([bitAvPol]).astype(np.float)
        avBitPol = np.mean(findBitPol, dtype=np.float64)
        print 'average bitcoin sentiment for the hour is:', avBitPol
        a = 'Bitcoin average/hr:', avBitPol

        findLitePol = np.array([liteAvPol]).astype(np.float)
        avLitePol = np.mean(findLitePol, dtype=np.float64)
        print 'average litecoin sentiment for the hour is:', avLitePol
        b = 'Litecoin average/hr:', avLitePol

        findEthPol = np.array([ethAvPol]).astype(np.float)
        avEthPol = np.mean(findEthPol, dtype=np.float64)
        print 'average Ethereum sentiment for the hour is:', avEthPol
        c = 'Ethereum average/hr:', avEthPol

            #findSub = np.array([Sub]).astype(np.float)
            #avSub = np.mean(findSub, dtype=np.float64)
        #print 'The average polarity of 10 most current tweets is:', avPol


        #*********MATPLOTLIB******
        # plot with various axes scales

        fig, axs = plt.subplots(2, 2, sharex=True)
        fig.subplots_adjust(left=0.08, right=0.98, wspace=0.1)
        #plt.title('Sentiment Analysis Graph\nof Cryptocurrency')#DOESNOTWORK
        #fig = plt.figure()

        #*******SENTIMENT GRAPH*******
        ax = axs[0, 0]
        #plt.plot(x,y1,label='Bitcoin')
        plot1 = ax.plot(x,y1,'red',label='Bitcoin') 
        #plt.plot(x,y2,label='Litecoin')
        plot2 = ax.plot(x,y2,'orange',label='Litecoin')
        #plt.plot(x,y3,label='Ethereum')
        plot3 = ax.plot(x,y3,'b-',label='Ethereum')

        ax.set_xlabel('Past Hour')
        ax.set_ylabel('Sentiment Comparisons')
        # Make the y-axis label, ticks and tick labels match the line color.
        #ax.set_ylabel('Sentiment', color='black')
        ax.tick_params('y', colors='black')
        ax2.margins(0.5)
        #ax.title('Sentiment Analysis Graph\nof Cryptocurrency')

        #ax.legend()
        #UPPER LEGEND
        #ax.legend( [ 'Lag ' + str(lag) for lag in all_x],loc='center right', bbox_to_anchor=(1.3, 0.5)


        #LOWER LEGEND
        # Shrink current axis's height by 10% on the bottom
        box = ax.get_position()
        ax.set_position([box.x0, box.y0 + box.height * 0.1,
                         box.width, box.height * 0.9])

        # Put a legend below current axis
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=5)

            #SAVE FIG TO PNG
        #fig.savefig('bitfig1.png', dpi=fig.dpi)
        #plt.show()

        #******BITCOIN PRICE/SENT GRAPH****

        ax = axs[0, 1]
        ax.plot(x, a1, 'black',label='Prices')
        ax.set_xlabel('Past Hour')
        # Make the y-axis label, ticks and tick labels match the line color.
        ax.set_ylabel('Bitcoin Price', color='black')
        ax.tick_params('y', colors='black')

        ax2 = ax.twinx()
        #s2 = np.sin(2 * np.pi * t)
        ax2.plot(x, y1, 'r-',label='Bitcoin Sentiment')
        ax2.set_ylabel('Bitcoin Sentiment', color='r')
        ax2.tick_params('y', colors='r')
        ax2.margins(0.5)
        #ax2.tick_params((-1.0, 1.0), colors='r')

        # Shrink current axis's height by 10% on the bottom
        box = ax.get_position()
        ax.set_position([box.x0, box.y0 + box.height * 0.1,
                         box.width, box.height * 0.9])

        # Put a legend below current axis
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=5)

        fig.tight_layout()
        #SAVE FIG TO PNG
        #fig.savefig('FAfig1.png', dpi=fig.dpi)

        #**********LITECOIN PRICE/SENT GRAPH******
        # log
        ax = axs[1, 1]
        #fig, ax1 = plt.subplots()
        #t = np.arange(0.01, 10.0, 0.01)
        #s1 = np.exp(t)
        ax.plot(x, a2, 'black',label='Litecoin Price')
        ax.set_xlabel('Past Hour')
        # Make the y-axis label, ticks and tick labels match the line color.
        ax.set_ylabel('Litecoin Price', color='black')
        ax.tick_params('y', colors='black')

        ax2 = ax.twinx()
        #s2 = np.sin(2 * np.pi * t)
        ax2.plot(x, y2, 'orange',label='Litecoin Sentiment')
        ax2.set_ylabel('Litecoin Sentiment', color='orange')
        ax2.tick_params('y', colors='orange')
        ax2.margins(0.5)
        #ax2.tick_params((-1.0, 1.0), colors='r')

        fig.tight_layout()
        #SAVE FIG TO PNG
        #fig.savefig('FAfig2.png', dpi=fig.dpi)
        #plt.show()

        #*******ETHEREUM PRICE/SENT GRAPH*******

        ax = axs[1, 0]
        ax.plot(x, a3, 'black',label='Ethereum Price')
        ax.set_xlabel('Past Hour')
        # Make the y-axis label, ticks and tick labels match the line color.
        ax.set_ylabel('Ethereum Price', color='black')
        ax.tick_params('y', colors='black')

        ax2 = ax.twinx()
        #s2 = np.sin(2 * np.pi * t)
        ax2.plot(x, y3, 'b-',label='Ethereum Sentiment')
        ax2.set_ylabel('Ethereum Sentiment', color='b')
        ax2.tick_params('y', colors='b')
        plt.ylim(-.2, .5)
        #ax2.tick_params((-1.0, 1.0), colors='r')
        #ax.legend()

        fig.tight_layout()
        #FIX DATES SHOWN ON BOTTOM OF GRAPH
        fig.autofmt_xdate()

        #SAVE FIG TO PNG
        fig.savefig('4g.png', dpi=fig.dpi)
      
        # ********TWITTER BOT PORTION OF CODE**************
                #This logs us in to twitter using the tweepy library
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

        api = tweepy.API(auth)

        #TWEETING GRAPH FROM SAVED PNG
        twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

        #photo_path = "Users/rachelgiles/Desktop/PythonProjects/dataAnalysis/sentAnalysis/bitfig1.png"
        photo_path = "4g.png"
        message = "Sentiment analyses of Bitcoin, Litecoin and Ethereum tweets and live prices, the past hour:"
        #twitter.update_status(status=myfig)
        api.update_with_media(photo_path, status=message)
        print("Tweeted: {}".format(message))


    #REMOVE CSV FILES TO BE REWRITTEN WITH A NEW HOUR'S DATA
        #os.remove('bitData.csv')
        #os.remove('liteData.csv')
        #os.remove('ethData.csv')
        os.remove('cryptData.csv')

    #CREATE NEW CSV WITH HEADER ONLY

        with open('cryptData.csv', 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter =",")
            writer.writerow(('avBitPol', 'bitPrice', 'avLitePol', 'litePrice', 'avEthPol', 'ethPrice', 'time'))

            

        #Every 5 minutes = 300secs
        #1 hour 3600 secs
        time.sleep(3600)

t1 = Thread(target = start1st)
t2 = Thread(target = start2nd)

t1.start()
time.sleep(100)
t2.start()


