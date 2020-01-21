from mongoConnection import Connection
import json


conn=Connection()
data=list(conn.getAllData())
s1=set(data[0].keys())
fields=["cloudCover", 
		"temperature", 
		"dewPoint", 
		"nearestStormBearing", 
		"windBearing", 
		"nearestStormDistance", 
		"visibility", 
		"apparentTemperature", 
		"pressure", 
		"humidity", 
		"ozone",
		"windSpeed", 
		"windGust", 
		"precipIntensity", 
		"uvIndex", 
		"precipProbability"]
s2=set(fields)
print(s1.difference(s2))
for d in data:
	newEntry={"result":{}, "meta":{}, "features":{}}
	for key in d:
		if key=="time":
			newEntry["meta"][key]=d[key]
		elif key=="rating":
			newEntry["result"][key]=d[key]
		elif key=="_id":
			newEntry[key]=d[key]
		else:
			newEntry["features"][key]=d[key]
	print(conn.collection.replace_one({"_id":d["_id"]}, newEntry))

		

		
