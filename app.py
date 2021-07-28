import tweepy
import os
from flask import Flask, render_template
from classes import *
from flask_apscheduler import APScheduler
import APIkeys

# domain = increazing.com by namecheap

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
def Twitter_Trends():
    t = api.trends_place(2352824)[0]['trends']
    twt_trends = []
    for i in t:
        name = i['name']
        url = i['url']
        twt_vol = i['tweet_volume']
        twt = Twt(title=name, link = url, volume=twt_vol)
        if twt_vol != None:
            twt_trends.append(twt)
    twt_trends.sort(reverse=True)
    twt_trends = twt_trends[:15]
    return twt_trends
#end of Twitter


#Entire database

def scheduleTask():
    print("Refetching data...")
    SocialMedias.clear()
    twitter_trend = Twitter_Trends()
    Twitter = Source(name="Twitter", posts = twitter_trend)
    SocialMedias.add(Twitter)
    print("Finished")


SocialMedias = Platforms()
scheduleTask()

app = Flask(__name__, static_folder= "static")
@app.route('/')
def home():
    data = SocialMedias
    return render_template("home.html", data = data)
if __name__ == '__main__':
    scheduler = APScheduler()
    scheduler.add_job(id="Scheduled task", func=scheduleTask, trigger="interval", seconds=600)
    scheduler.start()
    app.run(host = '0.0.0.0', port = 5000)