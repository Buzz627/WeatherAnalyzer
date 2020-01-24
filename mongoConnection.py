import pymongo
from dotenv import load_dotenv
import os

load_dotenv(".env")

class Connection:
	def __init__(self):
		if "DB_URL" in os.environ:
			client=pymongo.MongoClient(os.environ["DB_URL"])
		else:
			mongoUser=os.environ["DB_USER"]
			mongoPass=os.environ["DB_PASS"]
			client=pymongo.MongoClient(username=mongoUser, password=mongoPass)
		self.client=client
		db = client.weather
		self.collection = db[os.environ["DB_COLLECTION"]]

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
		

if __name__=="__main__":
	conn=Connection()
	data=conn.findData({"rating":4})
	for d in data:
		print(d)
# c=Connection()
# print(c.findData)