import requests
import json
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv(".env")

def getLocation():
	url = 'http://ipinfo.io/json'
	ipInfo=requests.get("https://ipinfo.io").json()
	print(ipInfo["city"])
	loc={"latitude":ipInfo["loc"].split(",")[0].strip(), "longitude": ipInfo["loc"].split(",")[1].strip() }
	return loc


def getForcast(loc=None):
	if loc==None:
		loc=getLocation()
		
		

	apiKey=os.environ["APIKEY"]
	lat=loc["latitude"]
	lon=loc["longitude"]
	print( lat, lon)
	r = requests.get('https://api.darksky.net/forecast/{}/{},{}'.format(apiKey, lat, lon))
	result=r.json()
	return result

def getCurrent(loc=None):
	if loc==None:
		loc=getLocation()
		

	return getForcast(loc)["currently"]

def getHourData(loc=None):
	return getForcast(loc)["hourly"]["data"]


if __name__ == "__main__":
	data=getHourData()

	for con in data:
		print(datetime.fromtimestamp(con["time"]))