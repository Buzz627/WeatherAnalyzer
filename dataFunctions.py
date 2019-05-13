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