import math

def average(lst):
	try:
		return math.fsum(lst)/len(lst)
	except: 
		return 0 

def sigma(lst):
	avg=average(lst)
	squares=map(lambda x: math.pow(x-avg, 2), lst) 
	meanSquares=math.fsum(squares)/len(lst)
	return math.sqrt(meanSquares)

def normilize(data, classification, fields=[]):
	normilizedData=list(map(lambda x: {classification:x[classification]}, data))
	if fields==[]:
		keys=data[0].keys()
	else:
		keys=fields

	for k in keys:
		try:
			avg=average(list(map(lambda x: x[k], data)))
			sig=sigma(list(map(lambda x: x[k], data)))
			for i in range(len(data)):
				normilizedData[i][k]=(data[i][k]-avg)/float(sig)

			
		except KeyError:
			print(">>>>>>> key error: "+ k)
			
		except TypeError as e: 
			# print(e)
			for i in range(len(data)):
				normilizedData[i][k]=data[i][k]
		
	return normilizedData