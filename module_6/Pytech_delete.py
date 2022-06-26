from pymongo import MongoClient
db=MongoClient.documents
db.collection.find({db.students})
print("DISPLAYING STUDENTS DOCUMENTS FROM FIND()QUERY"+db.students)
db.collection.insert_One(
   {"student_id":"1010"},
   {"First_name":"kevin"},
   {"Last_name":"drake"}
)
print("Inserting student 1010 to roster:"+db.students)
print("DELETE STUDENT ID: 1010:")
db.collection.delete_One(
   {"student_id":"1010"},
   {"First_name":"kevin"},
   {"Last_name":"drake"}
)
db.collection.find({db.students})
print("DISPLAYING NEW STUDENTS LIST DOC"+db.students)