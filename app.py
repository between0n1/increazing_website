import tweepy
import os
from flask import Flask, render_template
from classes import *
from flask_apscheduler import APScheduler
from waitress import serve
import APIkeys
import requests
import json
import dataGetter


# domain = increazing.com by namecheap

def scheduleTask():
    print("Refetching data...")
    SocialMedias.clear()
    twitter_trend = dataGetter.Twitter_Trends()
    reddit_trend = dataGetter.Reddit_Trends()
    Twitter = Source(name="Twitter", posts = twitter_trend)
    Reddit = Source(name="Reddit", posts = reddit_trend)
    SocialMedias.add(Twitter)
    SocialMedias.add(Reddit)
    print("Finished")


#Entire database

SocialMedias = Platforms() # Object containing social media name and its posts
scheduleTask()


app = Flask(__name__, static_folder= "static")
@app.route('/')
def home():
    data = SocialMedias
    return render_template("home.html", data = data)
if __name__ == '__main__':
    scheduler = APScheduler()
    scheduler.add_job(id="Scheduled task", func=scheduleTask, trigger= "interval", seconds= 300)
    scheduler.start()
    print("running")
    print(SocialMedias.sources)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    if os.environ.get('FLASK_ENV') == "development":
        app.run(host='0.0.0.0', port=5000)  # for test
    else:
        serve(app, host = '0.0.0.0', port = 5000)

