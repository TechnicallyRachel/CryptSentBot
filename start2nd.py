#This file takes the csv file of averages,
#graphs them and tweets them
#Then deletes the csv file to be re-written as a new file for a new hour

#GETTING NUMBERED LIST FROM CSV TEXT - Pandas
    
#THIS WORKS
#Example link: http://pythonforengineers.com/introduction-to-pandas/
# CALLING COLUMN HEADER WILL HAVE TO BE CHANGED IF CSV REWRITES ITSELF

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



while True:
    bitDataAv = pd.read_csv("bitData.csv", sep = ",")
    #print data.head()

    bitAvPol = bitDataAv["avPol"]
    #print Pol

    dfcall=bitDataAv.astype('datetime64[ns]')
    Time = dfcall["time"]
    print Time


    #data2 = data[["0.5", "2018-01-03 14:41:48.961986"]]




    # *************MATPLOTLIB***********

    # MATPLOTLIB

    #mdates.date2num(Time)


    x = Time
    #x = [Time]
    y = bitAvPol


    fig = plt.figure()
    plt.plot(x, y)

    plt.xlabel('Past hour')
    plt.ylabel('Sentiment')
    plt.title('Sentiment Analysis Graph\nof Bitcoin')
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
    message = "Sentiment analyses of bitcoin tweets, the past 5 minutes:"
    #twitter.update_status(status=myfig)
    api.update_with_media(photo_path, status=message)
    print("Tweeted: {}".format(message))


    os.remove('bitData.csv')

    with open('bitData.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter =",")
        writer.writerow(('avPol', 'time'))

    #Every 5 minutes = 300secs
    time.sleep(60)

    
