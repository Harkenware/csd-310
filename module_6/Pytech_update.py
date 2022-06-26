from pymongo import MongoClient
db=MongoClient.documents
db.collection.find({db.students})
print("DISPLAYING STUDENTS DOCUMENTS FROM FIND()QUERY"+db.students)
db.collection.updateOne(
   {"student_id":"1007"},
   {"$set":{"last_name":"daniels"}
   }
)
db.collection.find({"student_id":"1007"})
print("DISPLAYING UPDATED STUDENT DOCUMENT FROM FIND_ONE()QUERY"+db.james)