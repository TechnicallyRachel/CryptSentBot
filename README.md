# CryptSentBot
Cryptocurrency Sentiment Analysis Twitter Bot
Can be seen live at: https://twitter.com/cryptsentbot

Analysis of cryptocurrency (Bitcoin, Litecoin, Ethereum) twitter sentiment. Graphs of live data tweeted every hour. 

Programs used:
Twython, tweepy, TextBlob, matplotlib, Pandas, Numpy

There are two files that need to be executed. 

If you are going to play around with this code, I cannot state this enough #clear the csv files you create before re-running #your code!
#Also checking your csv files often is highly recommended.

98% of my bugs while creating this bot were because I had forgotten to clear the data recorded after the code had stopped in the middle of an execute.

#How I broke down the tweets into data:


#start1st.py
10 tweets each of "bitcoin", "litecoin" and "ethereum" keywords are searched (using tweepy) and analysed (TextBlob) using sentiment analysis (Polarity and Subjectivity are measured.)
The polarity, subjectivity and a current datetime stamp  3 different csv files. (bitDataTemp, liteDataTemp, ethDataTemp)
The average of those 10 tweets are taken (using numpy) and just the averaged polarity and a datetime stamp is recorded into a second corrolating csv file. (bitData, liteData, ethData)
The temp files are then deleted. A while loop is used to re-run the code every 30 seconds, recording the average polarity and time of tweet into the 2nd csv.

#start2nd.py 
The csv data is read as a string, not integers or floats, so the column data is extracted using pandas


#Manipulating the csv files

Step-bystep explination of code is in the comments.
