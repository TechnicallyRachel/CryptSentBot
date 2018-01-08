# CryptSentBot
Cryptocurrency Sentiment Analysis Twitter Bot
Can be seen live at: https://twitter.com/cryptsentbot

Analysis of cryptocurrency (Bitcoin, Litecoin, Ethereum) twitter sentiment. Graphs of live data tweeted every hour. 

**Programs used**
Twython, tweepy, TextBlob, matplotlib, Pandas, Numpy

**Code executed from Rasperry Pi for continuous tweeting

There are two files that need to be executed. 

If you are going to play around with this code, I cannot state this enough **empty the csv files you create before re-running your code! Also checking your csv files often is highly recommended.

98% of my bugs while creating this bot were because I had forgotten to clear the data recorded after the code had stopped in the middle of an execute.

**How I broke down the tweets into data:

**start1st.py**
10 tweets each of "bitcoin", "litecoin" and "ethereum" keywords are searched (using tweepy) and analysed (TextBlob) using sentiment analysis (Polarity and Subjectivity are measured.)
Three different for loops are created, one for each cryptocurrency.
The polarity, subjectivity and a current datetime stamp  3 different csv files. (bitDataTemp, liteDataTemp, ethDataTemp)
The average of those 10 tweets are taken (using numpy) and just the averaged polarity and a datetime stamp is recorded into a second corrolating csv file. (bitData, liteData, ethData)
The temp files are then deleted. A while loop is used to re-run the code every 30 seconds, recording the average polarity and time of tweet into the 2nd csv.

**start2nd.py**
The csv data is read as a string, not integers or floats, so the column data is extracted using pandas.

Using matplotlib, csv file data is used as plotted variables. 
"x = time" used from only bitData.csv since only one timestamp is needed. 
Graph is saved as .png

.png is then tweeted.

csv files are then removed, clearing them for the next hours data.

csv files with header row only created again.


**

***Step-by-step explination of code is in the comments***
