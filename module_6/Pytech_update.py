from pymongo import MongoClient
db=MongoClient.documents
db.collection.updateOne(
   {"student_id":"1007"},
   {"$set":{"last_name":"daniels"}
   }
)