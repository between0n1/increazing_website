from urllib import response
import requests
import json

query_params = {"platform_name" : "Twitter"}
end_point = 'https://www.api.increazing.com/api/recent'
response_api = requests.get(end_point).json()
for item in response_api['data']:
     if item['platform_name'] == "Twitter":
          print(item)