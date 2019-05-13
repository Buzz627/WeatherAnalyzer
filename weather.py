import requests
import json
from dotenv import load_dotenv
import os

load_dotenv(".env")

def getLocation():
	url = 'http://ipinfo.io/json'
	ipInfo=requests.get("https://ipinfo.io").json()
	return ipInfo


def getForcast():
	ipInfo=getLocation()

	apiKey=os.environ["APIKEY"]
	lat=ipInfo["loc"].split(",")[0].strip()
	lon=ipInfo["loc"].split(",")[1].strip()
	print(ipInfo["city"], lat, lon)
	r = requests.get('https://api.darksky.net/forecast/{}/{},{}?exclude=hourly,minutely,daily'.format(apiKey, lat, lon))
	result=r.json()
	return result

def getCurrent():
	return getForcast()["currently"]