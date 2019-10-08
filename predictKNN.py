from __future__ import division
from weather import getCurrent, getHourData, getDailyData
from dataFunctions import *
from mongoConnection import Connection
import json
from knnModel import Knn
from datetime import datetime


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

def predictHour(pos):
	conditions=getHourData(pos)
	conn=Connection()
	model=Knn(conn.getAllData(), "rating")
	model.trainFull()
	predictions=[]
	for i in conditions:
		normalPoint=normalizePoint(i, model.model["avg"], model.model["sig"])
		pred={"prediction":model.predict(normalPoint), "time": i["time"]}
		predictions.append(pred)
	return predictions

def prettyPrintHour(pos):
	data=predictHour(pos)
	result=""
	for i in data:
		date=datetime.fromtimestamp(i["time"])
		result+="{}: {}\n".format(date.strftime("%A: %I %p"), i["prediction"])
	return result

def predictDaily(pos):
	conditions=getDailyData(pos)
	conn=Connection()
	model=Knn(conn.getAllData(), "rating")
	model.trainFull()
	predictions=[]
	print(json.dumps(conditions[0], indent=4))
	for i in conditions:
		
		lowPoint=i.copy()
		highPoint=i.copy()
		minPoint=i.copy()
		maxPoint=i.copy()
		lowPoint["temperature"]=lowPoint["temperatureLow"]
		highPoint["temperature"]=highPoint["temperatureHigh"]
		minPoint["temperature"]=lowPoint["temperatureMin"]
		maxPoint["temperature"]=highPoint["temperatureMax"]

		normalLow=normalizePoint(lowPoint, model.model["avg"], model.model["sig"])
		normalHigh=normalizePoint(highPoint, model.model["avg"], model.model["sig"])
		normalMin=normalizePoint(minPoint, model.model["avg"], model.model["sig"])
		normalMax=normalizePoint(maxPoint, model.model["avg"], model.model["sig"])
		print(normalLow)
		pred={"prediction":{}, "time": i["time"]}
		pred["prediction"]["low"]=model.predict(normalLow)
		pred["prediction"]["high"]=model.predict(normalHigh)
		pred["prediction"]["min"]=model.predict(normalMin)
		pred["prediction"]["max"]=model.predict(normalMax)
		predictions.append(pred)
	return predictions

def prettyPrintDaily(pos):
	data=predictDaily(pos)
	result=""
	for i in data:
		date=datetime.fromtimestamp(i["time"])

		result+="{}: min:{con[min]} low:{con[low]} max:{con[max]} high:{con[high]}\n".format(date.strftime("%A"), con=i["prediction"])
	return result




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
	distances=[]
	for d in data:
		distances.append((getDistance(current, d), d))
	distances.sort(key=lambda x: x[0])
	k=5
	for i in range(k*2):
		print("{:.2f} {}".format(distances[i][0], distances[i][1]["rating"]))
		# print(distances[i])
	print("prediction:", average(list(map(lambda x: x[1]["rating"],distances[:k]))))



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

	print(prettyPrintDaily(None))
