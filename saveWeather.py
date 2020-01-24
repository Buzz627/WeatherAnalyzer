import requests
import json
import datetime
import sys
from dotenv import load_dotenv
import os
from weather import getCurrent
from mongoConnection import Connection

def save(rating, loc=None):
	now = datetime.datetime.now()

	currentResult={"result":{}, "meta":{}, "features":{}}
	condition=getCurrent(loc)
	currentResult["meta"]={
		"time":condition["time"], 
		"location":{
			"latitude":round(loc["latitude"], 3),
			"longitude":round(loc["longitude"], 3)}}
	del condition["time"]
	currentResult["features"]=condition

	currentResult["features"]['hour']=now.hour
	currentResult["features"]['month']=now.month
	currentResult["features"]['day']=now.day

	currentResult["result"]['rating']=rating
	
	conn=Connection()
	conn.insert_one(currentResult)
	# print(json.dumps(currentResult, indent=4))
	print("saved")


if  __name__=="__main__":
	if len(sys.argv) > 1:
		rating=int(sys.argv[1])
	else:
		rating=int(raw_input("enter rating: "))

	save(rating)

	



# print result.keys()
# print json.dumps(currentResult, indent=4)





