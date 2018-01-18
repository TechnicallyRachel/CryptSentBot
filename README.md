# CryptSentBot
# Work-In-Progress notes, scroll to bottom.
# MASTER.py contains all code used, all other files are snippets used for variations and unit testing.
Cryptocurrency Sentiment Analysis Twitter Bot
Can be seen live at: https://twitter.com/cryptsentbot

Analysis of cryptocurrency (Bitcoin, Litecoin, Ethereum) twitter sentiment.
Webscraped live prices of Bitcoin, Ethereum and Litecoin for comparison.
Graphs of live data tweeted every hour. 

**Libraries used**
Twython, tweepy, TextBlob, matplotlib, Pandas, Numpy

**Code executed from Rasperry Pi for continuous tweeting

If you are going to play around with this code, I cannot state this enough **empty the csv files you create before re-running your code! Also checking csv files often is highly recommended.

98% of my bugs while creating this bot were because I had forgotten to clear the data recorded after the code had stopped in the middle of an execute. Re-starting the MASTER file will rewrite the csv headers and graph will not read things correctly.

**How I parsed tweets into data:

**def start1st**
10 tweets each of "bitcoin", "litecoin" and "ethereum" keywords are searched (using tweepy) and analysed (TextBlob) using sentiment analysis (Polarity and Subjectivity are measured.) **Retweets ARE included

The polarity, subjectivity and a current datetime stamp is written into 3 different temp csv files. (bitDataTemp, liteDataTemp, ethDataTemp)
The average of those 10 tweets are taken (using numpy) and the averaged polarity, subjectivity and a datetime stamp is recorded into a second permanent csv file. (cryptData.py)
The temp files are then deleted. A while loop is used to re-run the code every 30 seconds, recording the average polarity and time of tweet into the 2nd csv.

**def start2nd**
The csv data is read as a string, not integers or floats, so the column data is extracted using pandas.

Using matplotlib, csv file data is used as plotted variables. 

Graph is saved as .png

.png is then tweeted.

csv files are then removed, clearing them for the next hours data.

csv files with header row only created again.


***Step-by-step explination of code is in the comments***

## Currently configuring AWS data pipeline (and AWS IoT to connect to RasPi where code is being run) to save data and easily import it to Tableau and Hadoop
## Currently creating and automating "Daily Update" graphs and vizualizations in Tableau that will be tweeted.
