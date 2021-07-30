import tweepy
import os
from flask import Flask, render_template
from classes import *
from flask_apscheduler import APScheduler
import APIkeys
import requests
import json


#Twitter
#API Keys
consumer_key = APIkeys.APIKEY
consumer_secret = APIkeys.APISecretKey
access_token = APIkeys.AccessToken
access_token_secret = APIkeys.AccessTokenSecret

#Twitter Authorization and Authentificatgion
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

#get trending twits
def Twitter_Trends(): # return array of trending twitter tweets
    t = api.trends_place(2352824)[0]['trends']
    twitter_trends = []
    for i in t:
        name = i['name']
        url = i['url']
        twitter_volume = i['tweet_volume']
        twt = Twitter(title=name, link = url, volume=twitter_volume)
        if twitter_volume != None:
            twitter_trends.append(twt)
    twitter_trends.sort(reverse=True)
    twitter_trends = twitter_trends[:10]
    return twitter_trends
#end of Twitter

#Reddit
def Reddit_Trends(): # return array of trending reddit posts
    reddit_url = 'https://www.reddit.com/r/popular/top/.json?raw_json=1'
    reddit_requests = requests.get(url = reddit_url ,headers = {'User-agent': 'increaZing'})
    reddit_data = reddit_requests.json()["data"]["children"][:15]
    reddit_trends = []
    for i in range(15):
        reddit_video_url = None
        reddit_img = None
        reddit_post = reddit_data[i]["data"]
        reddit_volume = reddit_post["score"]
        reddit_title = reddit_post["title"]
        reddit_author = reddit_post["author"]
        reddit_link = "http://www.reddit.com" + reddit_post["permalink"]
        if reddit_post["secure_media"] is not None:
            reddit_video_url = reddit_post["secure_media"]["reddit_video"]['hls_url']
        else:
            reddit_img = reddit_post["url"]

        red = Reddit(title=reddit_title, volume=reddit_volume, author=reddit_author, img=reddit_img, link=reddit_link, video=reddit_video_url)
        reddit_trends.append(red)


    return reddit_trends
# end of reddit
