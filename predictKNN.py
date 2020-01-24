from __future__ import division
from weather import getCurrent
from dataFunctions import *
from mongoConnection import Connection
import json


def getDistance(point1, point2):
	skip=["time", "rating"]
	total=0
	for key in point1:
		if key in skip:
			continue
		try:
			if key in point2:
				
				total+=abs(point1[key]-point2[key])
		except TypeError as e:
			continue
			print(e, "for key", key)
	return total

def predict(pos):
	current=getCurrent(pos)
	conn=Connection()
	data=list(conn.getAllData())
	data=list(map(lambda x: 
		{**x["features"], **{"rating":x["result"]["rating"]}, **{"_id":x["_id"]}}, data))
	nData=normalize(data, "rating")
	currentNormalized=normalizePoint(current, nData["avg"], nData["sig"])
	distances=[]
	for d in nData["data"]:
		distances.append((getDistance(currentNormalized, d), d))
	distances.sort(key=lambda x: x[0])
	k=5
	output=""
	for i in range(k*2):
		output+="{:.2f} {} {}\n".format(distances[i][0], distances[i][1]["rating"], distances[i][1]["_id"])
	output+="prediction: {}\n".format(average(list(map(lambda x: x[1]["rating"],distances[:k]))))
	return output



if __name__=="__main__":
	current={'visibility': 9.07, 
		'uvIndex': 4, 
		'apparentTemperature': 59.36, 
		'nearestStormBearing': 60, 
		'humidity': 0.85, 
		'pressure': 1024.08, 
		'dewPoint': 54.94, 
		'time': 1557327596, 
		'summary': 'Overcast', 
		'nearestStormDistance': 30, 
		'temperature': 59.36, 
		'windGust': 8.3, 
		'ozone': 326.64, 
		'windSpeed': 5.65, 
		'cloudCover': 1, 
		'precipIntensity': 0, 
		'windBearing': 69, 
		'precipProbability': 0, 
		'icon': 'cloudy'
	}
	current=getCurrent()
	conn=Connection()
	data=list(conn.getAllData())



	#raw Data
	distances=[]
	for d in data:
		distances.append((getDistance(current, d), d))
	distances.sort(key=lambda x: x[0])
	k=5
	for i in range(k*2):
		print("{:.2f} {}".format(distances[i][0], distances[i][1]["rating"]))
		# print(distances[i])
	print("prediction:", average(list(map(lambda x: x[1]["rating"],distances[:k]))))




	#normilized Data
	nData=normalize(data, "rating")
	currentNormalized=normalizePoint(current, nData["avg"], nData["sig"])
	distances=[]
	for d in nData["data"]:
		distances.append((getDistance(currentNormalized, d), d))
	distances.sort(key=lambda x: x[0])
	k=5
	for i in range(k*2):
		print("{:.2f} {} {}".format(distances[i][0], distances[i][1]["rating"], distances[i][1]["_id"]))
	print("prediction:", average(list(map(lambda x: x[1]["rating"],distances[:k]))))



	#standardized data
	sData=standardize(data, "rating")
	currentStandardize=standardizePoint(current, sData["high"], sData["low"])
	distances=[]
	for d in sData["data"]:
		distances.append((getDistance(currentStandardize, d), d))
	distances.sort(key=lambda x: x[0])
	k=5
	for i in range(k*2):
		print("{:.2f} {} {}".format(distances[i][0], distances[i][1]["rating"], distances[i][1]["_id"]))
	print("prediction:", average(list(map(lambda x: x[1]["rating"],distances[:k]))))

	print(getDistance(current, current))