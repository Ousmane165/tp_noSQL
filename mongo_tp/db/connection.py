from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["schoolDB"]
classes = db["classes"]