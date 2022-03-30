import tweepy
import os
from flask import Flask, render_template
from classes import *
from flask_apscheduler import APScheduler
import APIkeys
import requests
import json
import pytrends
import urllib
import urllib.request

# global var

TARGETPOSTNUM = 10

# Twitter
# API Keys
consumer_key = APIkeys.APIKEY
consumer_secret = APIkeys.APISecretKey
access_token = APIkeys.AccessToken
access_token_secret = APIkeys.AccessTokenSecret



# get trending twits
def Twitter_Trends():  # return array of trending twitter tweets
    query_params = {"platform_name" : "Twitter"}
    end_point = 'https://www.api.increazing.com/api/recent'
    response_api = requests.get(end_point).json()
    twitter_trends = []
    for item in response_api['data']:
        if item['platform_name'] == "Twitter":
            twt = Twitter(title = item["title"], link = item["oembed"], volume= item["volume"])
            twt.addTop(item["oembed"])
            twitter_trends.append(twt)
    return twitter_trends


# end of Twitter

# Reddit
def Reddit_Trends():  # return array of trending reddit posts
    reddit_url = 'https://www.reddit.com/r/popular/top/.json?raw_json=1'
    reddit_requests = requests.get(url=reddit_url, headers={'User-agent': 'increaZing'})
    try:
        reddit_data = reddit_requests.json()["data"]["children"][:TARGETPOSTNUM]
        reddit_trends = []
        for i in range(TARGETPOSTNUM):
            reddit_video_url = None
            reddit_img = None
            html = None
            reddit_post = reddit_data[i]["data"]
            reddit_volume = reddit_post["score"]
            reddit_title = reddit_post["title"]
            reddit_author = reddit_post["author"]
            reddit_link = "http://www.reddit.com" + reddit_post["permalink"]
            if reddit_post["secure_media"] is not None:
                if reddit_post["secure_media"].get("reddit_video", 0):
                    reddit_video_url = reddit_post["secure_media"]["reddit_video"]['hls_url']
                else:
                    try:
                        html = reddit_post["secure_media"]['oembed']['html']
                    except KeyError:
                        html = None
            else:
                if reddit_post['url'][-4] == ".":
                    reddit_img = reddit_post["url"]

            red = Reddit(title=reddit_title, volume=reddit_volume, author=reddit_author, img=reddit_img, link=reddit_link,
                         video=reddit_video_url, html=html)
            reddit_trends.append(red)
    except:
        reddit_trends = []
    return reddit_trends


# end of reddit


# Youtube
url = "https://www.googleapis.com/youtube/v3/videos?part=contentDetails&chart=mostPopular&regionCode=US&maxResults=10&key=" + APIkeys.GOOGLEAPIKEY


def Youtube_Trends():
    youtube_trends = []
    videos = (requests.get(url=url).json()['items'])
    for video in videos:
        video_src = "https://www.youtube.com/embed/" + (video['id'])

        # firstly, get top 10 trending youtube and we will fetch their title, viewcount using their id
        params = {'id': video['id'], 'key': APIkeys.GOOGLEAPIKEY,
                  'fields': 'items(id,snippet(channelId,title,categoryId),statistics)', 'part': 'snippet,statistics'}
        url_ = 'https://www.googleapis.com/youtube/v3/videos'
        query_string = urllib.parse.urlencode(params)
        url_ = url_ + "?" + query_string

        with urllib.request.urlopen(url_) as response:
            response_text = response.read()
            data = json.loads(response_text.decode())
            try:
                title = data['items'][0]['snippet']['title']
            except KeyError:
                title = "Unknown Title"
            try:
                viewCount = data['items'][0]['statistics']['viewCount']
            except KeyError:
                viewCount = 0
        You = Youtube(video=video_src, title=title, volume=viewCount)
        youtube_trends.append(You)
    youtube_trends.sort(reverse=True)
    return youtube_trends
