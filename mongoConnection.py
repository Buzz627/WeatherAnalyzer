import pymongo
from dotenv import load_dotenv
import os

load_dotenv(".env")

class Connection:
	def __init__(self):
		mongoUser=os.environ["DB_USER"]
		mongoPass=os.environ["DB_PASS"]
		client=pymongo.MongoClient(username=mongoUser, password=mongoPass)
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