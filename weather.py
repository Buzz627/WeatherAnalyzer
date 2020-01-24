import requests
import json
from dotenv import load_dotenv
import os

load_dotenv(".env")

def getLocation():
	url = 'http://ipinfo.io/json'
	ipInfo=requests.get("https://ipinfo.io").json()
	return ipInfo


def getForcast(loc):

	apiKey=os.environ["APIKEY"]
	lat=loc["latitude"]
	lon=loc["longitude"]
	print( lat, lon)
	# print('https://api.darksky.net/forecast/{}/{},{}?exclude=hourly,minutely,daily'.format(apiKey, lat, lon))
	r = requests.get('https://api.darksky.net/forecast/{}/{},{}?exclude=hourly,minutely,daily'.format(apiKey, lat, lon))
	result=r.json()
	return result

def getCurrent(loc=None):
	if loc==None:
		ipInfo=getLocation()
		print(ipInfo["city"])
		loc={"latitude":ipInfo["loc"].split(",")[0].strip(), "longitude": ipInfo["loc"].split(",")[1].strip() }

	return getForcast(loc)["currently"]