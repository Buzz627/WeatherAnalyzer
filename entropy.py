import pymongo
import json
import math


def makeBuckets(data, field, num):

	higest= max(map(lambda x: x[field], data))
	lowest= min(map(lambda x: x[field], data))

	bucketLen=float((higest-lowest)+1)/num
	buckets=[]

	for i in range(num):
		low= i*bucketLen+lowest
		high=(i+1)*bucketLen+lowest
		b=filter(lambda x: x[field] < high and x[field] >= low,data)
		buckets.append(b)
	# buckets[num-1].extend(filter(lambda x: x[field] == high,data))

	return buckets


def groupBy(data, field):
	result={}
	buckets=[]
	for i in data:
		key=str(i[field])
		if key not in result:
			result[key]=[]
		result[key].append(i)
	for b in result:
		buckets.append(result[b])
	return buckets

def entropy(data, classification):
	groups=groupBy(data, classification)
	total=0
	for g in groups:
		prob=float(len(g))/len(data)
		total -= (prob*math.log(prob, 2))
	return total

def informationGain(data, entropyField, classification):
	entropyBefore=entropy(data, classification)
	choices=makeBuckets(data, entropyField, 4)
	# print sum(map(lambda x: len(x), choices))
	entropyLst=[]
	for split in choices:
		prob=float(len(split))/len(data)
		entropyLst.append(prob*entropy(split, classification))
	entropyAfter= sum(entropyLst)


	return entropyBefore - entropyAfter



client=pymongo.MongoClient()
db = client.weather
collection = db.conditions

entropyField="cloudCover"

data=[]
results=collection.find({})
for d in results:
	# print d.keys()
	data.append(d)

# print data[0]

fields=["cloudCover", 
	"temperature", 
	"dewPoint", 
	# "nearestStormBearing", 
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

# buckets=makeBuckets(data, entropyField, 4)




infoGain=[]

for field in fields:
	infoGain.append((field, informationGain(data, field, "rating")))

infoGain.sort(key = lambda x: x[1])
for i in infoGain:
	print i

# data=[{"rating":"m", "ends-vowel":0}]*6
# data.extend([{"rating":"m", "ends-vowel":1}]*3)
# data.extend([{"rating":"f", "ends-vowel":0}]*1)
# data.extend([{"rating":"f", "ends-vowel":1}]*4)
# entropyField="ends-vowel"

# print informationGain(data, entropyField, "rating")












# print json.dumps(data)


