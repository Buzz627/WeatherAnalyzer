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


	currentResult=getCurrent(loc)
	currentResult['hour']=now.hour
	currentResult['month']=now.month
	currentResult['day']=now.day

	currentResult['rating']=rating
	conn=Connection()
	conn.insert_one(currentResult)
	# print(currentResult)
	print("saved")


if  __name__=="__main__":
	if len(sys.argv) > 1:
		rating=int(sys.argv[1])
	else:
		rating=int(raw_input("enter rating: "))

	save(rating)

	



# print result.keys()
# print json.dumps(currentResult, indent=4)





