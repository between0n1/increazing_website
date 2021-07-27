import tweepy
import os
from flask import Flask, render_template
from classes import *
import APIkeys

# domain = increazing.com by namecheap

#Twitter
#API Keys
consumer_key = APIkeys.APIKEY
consumer_secret = APIkeys.APISecretKey
access_token = APIkeys.AccessToken
access_token_secret = APIkeys.AccessTokenSecret

#Authorization and Authentificatgion
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#get trending twits
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
#end of Twitter

#Entire database
SocialMedias = Platforms()
Twitter = Source(name="Twitter", posts = twt_trends)
SocialMedias.add(Twitter)



app = Flask(__name__, static_folder= "static")
@app.route('/')
def home():
    data = SocialMedias
    return render_template("home.html", data = data)
if __name__ == '__main__':
    # sort by tweet_volume
    app.run(host = '0.0.0.0', port = 5000)