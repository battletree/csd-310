from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.lifch.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client =MongoClient(url)

db = client.pytech

print("-- pytech Collection List --")
print(db.list_collection_names())

students = db.get_collection("students")

print("--DISPLAYING STTUDENTS DOCUMENTS FROM find() QUERY--")
doc=db.students.find_one({"student_id":"1007"})
print("Student ID: " + doc["student_id"])
print("First Name: " + doc["first_name"])
print("Last Name: " + doc["last_name"])


doc=db.students.find_one({"student_id":"1008"})
print("Student ID: " + doc["student_id"])
print("First Name: " + doc["first_name"])
print("Last Name: " + doc["last_name"])


doc=db.students.find_one({"student_id":"1009"})
print("Student ID: " + doc["student_id"])
print("First Name: " + doc["first_name"])
print("Last Name: " + doc["last_name"])

