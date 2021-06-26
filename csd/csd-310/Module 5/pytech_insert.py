from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.lifch.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client =MongoClient(url)

db = client.pytech

print("-- pytech Collection List --")
print(db.list_collection_names())

eugene = {
    "first_name": "Eugene",
    "last_name": "kwon",
    "student_id": "1007"
}
owen = {
    "first_name": "owen",
    "last_name": "hoff",
    "student_id": "1008"
}
david = {
    "first_name": "david",
    "last_name": "louch",
    "student_id": "1009"
}

students = db.get_collection("students")

students.drop()

eugene_student_id = students.insert_one(eugene).inserted_id
hoff_student_id = students.insert_one(owen).inserted_id
david_student_id = students.insert_one(david).inserted_id

print("INSERT STATEMENTS")
print("Inserted student record Eugene Kwon into the students collection with document_id " + str(eugene_student_id))
print("Inserted student record Owen Hoff into the students collection with document_id " + str(hoff_student_id))
print("Inserted student record David Louch into the students collection with document_id " + str(david_student_id))
