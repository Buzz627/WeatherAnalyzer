import matplotlib.pyplot as plt
import pymongo
import json


client=pymongo.MongoClient()
db = client.weather
collection = db.conditions
colors={"1":"r", "2":"#FFA500", "3":"#FFFF00", "4":"b", "5":"#00FF00"}
for r in colors:

	data=collection.find({"rating":int(r)}, {"temperature":1, "pressure":1, "precipProbability":1})
	x=[] 
	y=[]

	for i in data:
		x.append(i['temperature'])
		y.append(i['pressure'])
		plt.plot(x,y, 'o',color=colors[r])
		# print i
plt.show()
