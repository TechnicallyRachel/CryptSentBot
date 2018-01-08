

# analyse data from bitcoin, litecoin and ethereum
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



#Write initial csv (to be deleted) outside loop to get just 1 header
# If inside loop - will write header for each tweet
#Will not average properly
with open('bitData.csv', 'a') as csv_file:
    writer = csv.writer(csv_file, delimiter =",")
    writer.writerow(('avPol', 'time'))

with open('liteData.csv', 'a') as csv_file:
    writer = csv.writer(csv_file, delimiter =",")
    writer.writerow(('avPol', 'time'))


with open('ethData.csv', 'a') as csv_file:
    writer = csv.writer(csv_file, delimiter =",")
    writer.writerow(('avPol', 'time'))


def start1st():
    while True:
        #Write all temp csv files
        with open('bitDataTemp.csv', 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter =",")
            writer.writerow(('Pol', 'Sub', 'time'))

        with open('liteDataTemp.csv', 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter =",")
            writer.writerow(('Pol', 'Sub', 'time'))

        
        with open('ethDataTemp.csv', 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter =",")
            writer.writerow(('Pol', 'Sub', 'time'))
                            
        
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
                
            #Step 4 Perform Sentiment Analysis on Tweets
            analysis = TextBlob(tweet.text)

            #a = analysis.sentiment.polarity
            #b = analysis.sentiment.subjectivity
    #        print(analysis.sentiment)
                
    #        print("")
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


    #***************LITECOIN PORTION*****************


        for tweet in litecoin_tweets:
            
            #tweet.lang == "en"
    #        print(tweet.text)
                
            #Step 4 Perform Sentiment Analysis on Tweets
            analysis = TextBlob(tweet.text)

            #a = analysis.sentiment.polarity
            #b = analysis.sentiment.subjectivity
    #        print(analysis.sentiment)
                
    #        print("")
            # data.append http://altitudelabs.com/blog/web-scraping-with-python-and-beautiful-soup/
            
            #WRITING CSV FILE 1 - THIS CSV WILL NEED TO WRITE OVER ITSELF
            #(Make sure this is within the "for tweet" for loop to save each tweet info correctly)
            #insert for loop here?

            with open('liteDataTemp.csv', 'a') as csv_file: #a = append MUST STAY 'a'
                # OR for loop here(?)
                # TextBlob parsing info: http://textblob.readthedocs.io/en/dev/quickstart.html#sentiment-analysis

                writer = csv.writer(csv_file, delimiter =",")
                writer.writerow([analysis.sentiment.polarity,
                    analysis.sentiment.subjectivity, datetime.datetime.now()])


            # Extract [Pol] as numbered list variable using pandas
            data = pd.read_csv("liteDataTemp.csv", sep = ",")
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


        with open('liteData.csv', 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter =",")
                    #writer.writerow((0, 0.0, 0.00))
            writer.writerow([avPol, datetime.datetime.now()])

    #****************ETHEREUM PORTION****************


        for tweet in ethereum_tweets:
            
            #tweet.lang == "en"
    #        print(tweet.text)
                
            #Step 4 Perform Sentiment Analysis on Tweets
            analysis = TextBlob(tweet.text)

            #a = analysis.sentiment.polarity
            #b = analysis.sentiment.subjectivity
    #        print(analysis.sentiment)
                
    #        print("")
            # data.append http://altitudelabs.com/blog/web-scraping-with-python-and-beautiful-soup/
            
            #WRITING CSV FILE 1 - THIS CSV WILL NEED TO WRITE OVER ITSELF
            #(Make sure this is within the "for tweet" for loop to save each tweet info correctly)
            #insert for loop here?

            with open('ethDataTemp.csv', 'a') as csv_file: #a = append MUST STAY 'a'
                # OR for loop here(?)
                # TextBlob parsing info: http://textblob.readthedocs.io/en/dev/quickstart.html#sentiment-analysis

                writer = csv.writer(csv_file, delimiter =",")
                writer.writerow([analysis.sentiment.polarity,
                    analysis.sentiment.subjectivity, datetime.datetime.now()])


            # Extract [Pol] as numbered list variable using pandas
            data = pd.read_csv("ethDataTemp.csv", sep = ",")
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


        with open('ethData.csv', 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter =",")
                    #writer.writerow((0, 0.0, 0.00))
            writer.writerow([avPol, datetime.datetime.now()])

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
        bitDataAv = pd.read_csv("bitData.csv", sep = ",")
        liteDataAv = pd.read_csv("liteData.csv", sep = ",")
        ethDataAv = pd.read_csv("ethData.csv", sep = ",")
        #print data.head()

        bitAvPol = bitDataAv["avPol"]
        print bitAvPol
        liteAvPol = liteDataAv["avPol"]
        print liteAvPol
        ethAvPol = ethDataAv["avPol"]
        #print Pol

        dfcall=bitDataAv.astype('datetime64[ns]')
        Time = dfcall["time"]
        print Time

        #data2 = data[["0.5", "2018-01-03 14:41:48.961986"]]


        # *************MATPLOTLIB***********

        x = Time
        #x = [Time]
        y1 = bitAvPol
        y2 = liteAvPol
        y3 = ethAvPol


        fig = plt.figure()

        #ax = plt.axes(y1, y2)
        #ax.yrange(
        #ax.plot(x, y1, y2)

        #ylim is a function of pyplot - limits y axis
        plt.ylim(-2.0, 2.0)

        plt.plot(x,y1,label='Bitcoin')
        plt.plot(x,y2,label='Litecoin')
        plt.plot(x,y3,label='Ethereum')
        
        plt.xlabel('Past 1 hour')
        plt.ylabel('Sentiment')
        plt.title('Sentiment Analysis Graph\nof Cryptocurrency')
        #plt.legend('Bitcoin', 'Litecoin', 'Ethereum')
        plt.legend()

        #plt.show()

        #SAVE FIG TO PNG
        fig.savefig('bitfig1.png', dpi=fig.dpi)


        #plt.close(fig)


        # ********TWITTER BOT PORTION OF CODE**************
                #This logs us in to twitter using the tweepy library
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

        api = tweepy.API(auth)

        #TWEETING GRAPH FROM SAVED PNG
        twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

        #photo_path = "Users/rachelgiles/Desktop/PythonProjects/dataAnalysis/sentAnalysis/bitfig1.png"
        photo_path = "bitfig1.png"
        message = "Sentiment analyses of bitcoin tweets, the past hour:"
        #twitter.update_status(status=myfig)
        api.update_with_media(photo_path, status=message)
        print("Tweeted: {}".format(message))


    #REMOVE CSV FILES TO BE REWRITTEN WITH A NEW HOUR'S DATA
        os.remove('bitData.csv')
        os.remove('liteData.csv')
        os.remove('ethData.csv')

    #CREATE NEW CSV'S WITH HEADER ONLY
        with open('bitData.csv', 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter =",")
            writer.writerow(('avPol', 'time'))
            
        with open('liteData.csv', 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter =",")
            writer.writerow(('avPol', 'time'))

        with open('ethData.csv', 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter =",")
            writer.writerow(('avPol', 'time'))
            

        #Every 5 minutes = 300secs
        #1 hour 3600 secs
        time.sleep(3600)



t1 = Thread(target = start1st)
t2 = Thread(target = start2nd)

t1.start()
time.sleep(100)
t2.start()
