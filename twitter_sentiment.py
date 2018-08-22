# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 18:02:32 2018
@author: Amit
"""
import csv
import tweepy
from textblob import TextBlob
from unidecode import unidecode
import matplotlib.pyplot as plt

# Step 1 - Authenticate
consumer_key = "xxxxxxxxxxxxxx"
consumer_secret = "xxxxxxxxxxxxxx"
access_token = "xxxxxxxxxxxxxxxxxxxxxxxxx"
access_token_secret = "xxxxxxxxxxxxxxxxxxxxxxx"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


## search Twitter for something that interests you
query = input("What subject do you want to analyze for this example? \n")
## enter the number of tweets you want to analyze
number = input("How many Tweets do you want to analyze? \n")
     
     
 
def drawing_pie(pos, neg, nue):
    #Calculating positive,negative and neutral counts as percentage values
    total = float(pos)+float(neg)+float(neu)
    positive = round((pos/total)*100,1)
    negative = round((neg/total)*100,1)
    neutral = round((neu/total)*100,1)
 
    #Creating lists such as sentiments,label and cols to draw pie chart
    sentiments =[positive,negative,neutral]
    label =['Positive','Negative','Neutral']
    cols = ['g','r','b']
 
    #Creating Pie Chart using matplotlib.pyplot
    plt.pie(sentiments,labels=label,colors=cols,autopct='%1.1f%%',shadow=True)
 
    #Creating a title for the pie chart based on the overall sentiment
    if positive > negative:
        if positive > neutral or negative == neutral:
            plt.title ('Sentiment is Positive')     
    if negative > positive:
        if negative > neutral or positive == neutral:
            plt.title ('Sentiment is Negative')
    if neutral >= positive and neutral >= negative:
        plt.title ('Sentiment is Neutral')
    if positive == negative:
        plt.title ('Sentiment is Neutral')
 
    #Saving the pie chart
    plt.savefig('C:/Users/Amit/Desktop/python/Sentiment_Pie.png')
 
    #Returning the result
    return plt.show()
         
     
     
     
## open a csv file to store the Tweets and their sentiment 
file_name = 'Sentiment_Analysis_of_{}_Tweets_About_{}.csv'.format(number, query)

with open(file_name, 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', lineterminator='\n')

    #Save each Tweet to a CSV file
    writer.writerow(['Tweet', 'Polarity', 'Subjectivity'])
    
    
    times = int(number) / 100
    number = 100
    pos = 0
    neg = 0
    neu = 0
    
    while times > 0:
        times -= 1
        public_tweets = api.search(
           lang="en",
           q=query + " -rt",
           count=number,
           result_type="recent"
        )
    
        for tweet in public_tweets:
            analysis = TextBlob(unidecode(tweet.text))
            if(analysis.sentiment.polarity > 0.1):
                pos +=1
                writer.writerow([unidecode(tweet.text), 'positive', analysis.sentiment.subjectivity])
            elif(analysis.sentiment.polarity < -0.1):
                neg +=1
                writer.writerow([unidecode(tweet.text), 'negative', analysis.sentiment.subjectivity])
            else:
                neu +=1
                writer.writerow([unidecode(tweet.text), 'neutral', analysis.sentiment.subjectivity]) 
    
    drawing_pie(pos, neg, neu)
