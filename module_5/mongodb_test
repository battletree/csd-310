#Mitchell Kwon
#CSD 310
#6/23/21
#connecting to MongoDB

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.lifch.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client =MongoClient(url)

db = client.pytech

print("-- pytech Collection List --")
print(db.list_collection_names())
