from __future__ import division
from weather import getCurrent
from dataFunctions import average
from mongoConnection import Connection


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
	data=conn.getAllData()
	distances=[]
	for d in data:
		distances.append((getDistance(current, d), d))
	distances.sort()
	k=5
	# for i in range(len(distances)):
	# 	print(distances[i][0], distances[i][1]["rating"])
	print("prediction:", average(list(map(lambda x: x[1]["rating"],distances[:k]))))
