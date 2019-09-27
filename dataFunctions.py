import math

def average(lst):
	try:
		return math.fsum(lst)/len(lst)
	except: 
		return 0 
def mode(lst):
	return max(set(lst), key = lst.count)

def sigma(lst):
	avg=average(lst)
	squares=map(lambda x: math.pow(x-avg, 2), lst) 
	meanSquares=math.fsum(squares)/len(lst)
	return math.sqrt(meanSquares)

def round(num):
	return int(num+0.5)

def RMSE(lst):
	totalDifferance=math.fsum(list(map(lambda x: x[0]-x[1], lst)))

	return math.sqrt((totalDifferance**2)/len(lst))


def normalizePoint(point, avg, sig):
	newPoint={}
	for key in point:
		try:
			newPoint[key]=(point[key]-avg[key])/sig[key]

		except KeyError:
			continue
			print(">>>>>>> key error: "+ key)
			
		# except TypeError as e: 
		# 	# print(e)
		# 	for i in range(len(data)):
		# 		normalized[i][k]=data[i][k]
	return newPoint


def normalize(data, classification, fields=[]):
	normalizedData=list(map(lambda x: {classification:x[classification]}, data))
	if fields==[]:
		keys=data[0].keys()
	else:
		keys=fields

	metadata={"avg":{}, "sig":{}}
	for k in keys:
		if k==classification:
			continue
		try:
			avg=average(list(map(lambda x: x[k], data)))
			sig=sigma(list(map(lambda x: x[k], data)))
			metadata["avg"][k]=avg
			metadata["sig"][k]=sig
			for i in range(len(data)):
				normalizedData[i][k]=(data[i][k]-avg)/float(sig)

			
		except KeyError:
			print(">>>>>>> key error: "+ k)
			
		except TypeError as e: 
			# print(e)
			for i in range(len(data)):
				normalizedData[i][k]=data[i][k]
		
	return {"data":normalizedData, **metadata}

def standardizePoint(point, high, low):
	newPoint={}
	for key in point:
		try:
			newPoint[key]=(point[key]-low[key])/(high[key]-low[key])

		except KeyError:
			print(">>>>>>> key error: "+ key)
			
		except TypeError as e: 
			pass
		# 	# print(e)
		# 	for i in range(len(data)):
		# 		normalized[i][k]=data[i][k]
	return newPoint

def standardize(data, classification, fields=[]):
	standardData=list(map(lambda x: {classification:x[classification]}, data))
	if fields==[]:
		keys=data[0].keys()
	else:
		keys=fields
	metadata={"high":{},"low":{}}

	for k in keys:
		try:
			low=min(list(map(lambda x: x[k], data)))
			high=max(list(map(lambda x: x[k], data)))
			metadata["high"][k]=high
			metadata["low"][k]=low
			for i in range(len(data)):
				if k != classification:
					standardData[i][k]=(data[i][k]-low)/(high-low)
		except KeyError:
			print(">>>>>>> key error: "+ k)
			
		except TypeError as e: 
			# print(e)
			for i in range(len(data)):
				standardData[i][k]=data[i][k]

	return {"data":standardData, **metadata}
