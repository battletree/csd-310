#Mitchell D. Kwon
#CSD 310   
#learning how to delete

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

#building test document
test_doc = {
    "student_id": "1010",
    "first_name": "Ryan",
    "last_name": "Slapnovsky"
}

#inserting test document
test_doc_id = students.insert_one(test_doc).inserted_id

#insert statements
print("\n -- INSERT STATEMENTS--")
print(" Inserted student record into the students collection with document_id " + str(test_doc_id))

#using find_one() method for student_id 1010
student_test_doc = students.find_one({"student_id": "1010"})

#printing the results
print("\n --DISPLAYING STUDENT TEST DOC --")
print(" Student ID: " + student_test_doc["student_id"] + "\n First Name: " + student_test_doc["first_name"] + "\n Last Name: " + student_test_doc["last_name"] + "\n")

#using the delete_one method in order to remove the student_test_doc
delted_student_test_doc = students.delete_one({"student_id": "1010"})

#finding all students
new_student_list = students.find({})

#display message
print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

#loop the collection and output
for doc in new_student_list:
    print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

#end message
input("\n\n End of program, press any key to continue...")