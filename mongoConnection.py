import pymongo

class Connection:
	def __init__(self):
		client=pymongo.MongoClient()
		self.client=client
		db = client.weather
		self.collection = db.conditions

	def getAllData(self):
		result=self.collection.find({})
		return result

	def findData(self, *query):
		result=self.collection.find(*query)
		return result

	def insert_one(self, data):
		self.collection.insert_one(data)

	def close(self):
		self.client.close()
		


# c=Connection()
# print(c.findData)