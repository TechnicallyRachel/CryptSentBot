
#Find other sentiment analyses code that calls more tweets at a time
# or just cron job this at faster rate?
#research how to input data to csv files
#research how to visualize data from csv file in piechart/graph- matplotlib?
# analyse data from bitcoin, litecoin and ethereum(?)
#TRYING TO GET A FOR LOOP FOR THE CSV FILE
#NEEDS TO WRITE OVER ITSELF EVERY 3MINUTES
# analyse data from bitcoin, litecoin and ethereum(?)
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
import os



#Write initial csv (to be deleted) outside loop to get just 1
# If inside loop - will write header for each tweet
#Will not average properly
with open('bitData.csv', 'a') as csv_file:
    writer = csv.writer(csv_file, delimiter =",")
    writer.writerow(('avPol', 'time'))



while True:
    with open('bitDataTemp.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter =",")
        writer.writerow(('Pol', 'Sub', 'time'))
            

        #This logs us in to twitter using the tweepy library
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

        api = tweepy.API(auth)

    #Step 3 - Retrieve Tweets

    public_tweets = api.search('bitcoin', count=5)

        #public_tweets = api.search(" -RT", 'bitcoin', count=10)

        # BITCOIN SENTIMENT ANALYSIS AND CSV FILE WRITING
        #data = []


    for tweet in public_tweets:
        
        #tweet.lang == "en"
        print(tweet.text)
            
        #Step 4 Perform Sentiment Analysis on Tweets
        analysis = TextBlob(tweet.text)

        #a = analysis.sentiment.polarity
        #b = analysis.sentiment.subjectivity
        print(analysis.sentiment)
            
        print("")
        # data.append http://altitudelabs.com/blog/web-scraping-with-python-and-beautiful-soup/
        
        #WRITING CSV FILE 1 - THIS CSV WILL NEED TO WRITE OVER ITSELF
        #(Make sure this is within the "for tweet" for loop to save each tweet info correctly)
        #insert for loop here?

        with open('bitDataTemp.csv', 'a') as csv_file: #a = append MUST STAY 'a'
            # OR for loop here(?)
            # TextBlob parsing info: http://textblob.readthedocs.io/en/dev/quickstart.html#sentiment-analysis

            writer = csv.writer(csv_file, delimiter =",")
            writer.writerow([analysis.sentiment.polarity,
                analysis.sentiment.subjectivity, datetime.datetime.now()])


        # Extract [Pol] as numbered list variable using pandas
        data = pd.read_csv("bitDataTemp.csv", sep = ",")
        Pol = data['Pol']
        #Sub = data["0.0"]
                    
        #FIND THE AVERAGE POL AND SUB
            #THIS ALL WORKS - FROM NUMPY
        findPol = np.array([Pol]).astype(np.float)
        avPol = np.mean(findPol, dtype=np.float64)
            #findSub = np.array([Sub]).astype(np.float)
            #avSub = np.mean(findSub, dtype=np.float64)
        print 'The average polarity of 10 most current tweets is:', avPol
            #print 'The average subjectivity of 10 most current tweets is:', avSub


    with open('bitData.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter =",")
                #writer.writerow((0, 0.0, 0.00))
        writer.writerow([avPol, datetime.datetime.now()])

        #DELETE 1st temp CSV file - the one with tweets to be averaged.
    os.remove('bitDataTemp.csv')
 
    time.sleep(10)
