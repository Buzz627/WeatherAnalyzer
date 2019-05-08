import requests
import pymongo
import json
import datetime
import sys
from dotenv import load_dotenv
import os

load_dotenv(".env")

if len(sys.argv) > 1:
	rating=int(sys.argv[1])
else:
	rating=int(raw_input("enter rating: "))


url = 'http://ipinfo.io/json'
ipInfo=requests.get("https://ipinfo.io").json()


apiKey=os.environ["APIKEY"]
lat=ipInfo["loc"].split(",")[0].strip()
lon=ipInfo["loc"].split(",")[1].strip()
print(ipInfo["city"], lat, lon)

now = datetime.datetime.now()
client=pymongo.MongoClient()
db = client.weather
collection = db.conditions
r = requests.get('https://api.darksky.net/forecast/{}/{},{}?exclude=hourly,minutely,daily'.format(apiKey, lat, lon))
result=r.json()
currentResult=result['currently']
currentResult['hour']=now.hour
currentResult['month']=now.month
currentResult['day']=now.day

currentResult['rating']=rating

collection.insert_one(currentResult)
print("saved")
# print result.keys()
# print json.dumps(currentResult, indent=4)





