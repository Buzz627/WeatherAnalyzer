from mongoConnection import Connection
from dataFunctions import *
import random


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

class Knn():
	def __init__(self, data, classification):
		self.data=list(data)
		self.classification=classification

	def split(self, trainLimit):
		index=int(len(self.data)*(trainLimit/100))
		shuffled=random.sample(self.data, len(self.data))
		self.trainingSet=shuffled[:index]
		self.testingSet=shuffled[index:]

	def train(self):
		self.model=normalize(self.trainingSet, self.classification)

	def predict(self, point, k=5):
		distances=[]
		for d in self.model["data"]:
			distances.append((getDistance(point, d), d))
		distances.sort()
		return average(list(map(lambda x: x[1][self.classification],distances[:k])))

	def test(self):
		mat=[[0]*5 for _ in range(5)]
		predictionLst=[]
		for point in self.testingSet:
			normalPoint=normalizePoint(point, self.model["avg"], self.model["sig"])
			prediction=self.predict(normalPoint)
			j=round(prediction)-1
			i=point[self.classification]-1
			mat[i][j]+=1
			print(point["rating"], prediction)
			predictionLst.append((point[self.classification], prediction))
		for l in mat:
			print(l)
		print()
		print(RMSE(predictionLst))



if __name__=="__main__":
	conn=Connection()
	model=Knn(conn.getAllData(), "rating")
	for i in range(5):
		model.split(90)
		model.train()
		model.test()
