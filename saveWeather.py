import requests
import json
import datetime
import sys
from dotenv import load_dotenv
import os
from weather import getCurrent
from mongoConnection import Connection

if  __name__=="__main__":
	if len(sys.argv) > 1:
		rating=int(sys.argv[1])
	else:
		rating=int(raw_input("enter rating: "))



	now = datetime.datetime.now()


	currentResult=getCurrent()
	currentResult['hour']=now.hour
	currentResult['month']=now.month
	currentResult['day']=now.day

	currentResult['rating']=rating
	conn=Connection()
	conn.insert_one(currentResult)
	print("saved")



# print result.keys()
# print json.dumps(currentResult, indent=4)





