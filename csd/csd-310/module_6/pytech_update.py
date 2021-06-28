#Mitchell D. Kwon
# CSD 310   
# learning how to update

#import statements
from pymongo import MongoClient

#MongoDB connection string
url = "mongodb+srv://admin:admin@cluster0.lifch.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

#connecting to the MongoDB cluster
client =MongoClient(url)

#connecting to the pytech database
db = client.pytech

#grabbing the students collection
students = db.students

#finding all of the students in my collection
student_list = students.find({})

#print message
print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

#loop collection and output results
for doc in student_list:
    print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

#Updating student id 1007 from Kwon to Dai
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Dai"}})

#finding the updated student
eugene = students.find_one({"student_id": "1007"})

#print message
print("\n -- DISPLAYING STUDENT DOCUMENT 1007 --")

#printing the updated document to the terminal window
print(" Student ID: " + eugene["student_id"] + "\n First Name: " + eugene["first_name"] + "\n Last Name: " + eugene["last_name"] + "\n")

#printing end message
input("\n\n End of program, press any key to continue...")