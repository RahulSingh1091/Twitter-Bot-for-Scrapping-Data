# -*- coding: utf-8 -*-
"""
Created on Sun May 13 05:49:24 2018

@author: singh
"""

import tweepy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
import textblob


consumer_key = 'YpleO1o1khgZz1ydsdsdslUs5OPS0'
consumer_secret = 'eZrQ3yA30sal96al9HWsdsddsjcZCeU4X8xOIjDg6BVXW7If5'
access_token = '244860913-B4vp1bmdssdsdssdDhzJR3aRnihXOkx7uRVjfgt'
access_token_secret = 'yi1guv8WElJv8V9e0yw5CdsdsdQmuzgbINQIQ9au3GLsNB'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

message,favorite_count,retweet_count,created_at,user_name,favourites_count,description,friends_count,followers_count=[],[],[],[],[],[],[],[],[]
for status in tweepy.Cursor(api.user_timeline, id="Test_Tweeter_Profile ").items(100):
    message.append(status.text)
    favorite_count.append(status.favorite_count)
    retweet_count.append(status.retweet_count)
    created_at.append(status.created_at)
    user_name.append(status.user.name)
    favourites_count.append(status.user.favourites_count)
    description.append(status.user.description)
    friends_count.append(status.user.friends_count)
    followers_count.append(status.user.followers_count)
    
    
df=pd.DataFrame({'Message':message,
                'Tweet Favorite Count':favorite_count,
                'Retweet Count':retweet_count,
                'Created At':created_at,
                'Username':user_name,
                'Likes':favourites_count,
                'User Description':description,
                'Following':friends_count,
                'Followers':followers_count})
df.to_csv("Twitter Timeline.csv")
print(df)





  



