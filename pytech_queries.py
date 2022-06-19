from pymongo import MongoClient
db=MongoClient.database
collection= db.students
docs= db.students.find({})
doc=db.students.find_one({james})
print(doc[james])