from pymongo import MongoClient
db=MongoClient.documents
collection= db.students
#each student is given information to be inserted into the collection later
james = {
    "first_name": "james", 
    "last_name":"cooper",
    "student_id":"1007"
 }
rick = {
    "first_name": "rick", 
    "last_name":"james",
    "student_id":"1008"
}
thom = {
    "first_name": "thom", 
    "last_name":"oneil",
    "student_id":"1009"
}
#insert student information into the collection using the insert_one method
student_id1=collection.insert_one(james).students
student_id2=collection.insert_one(rick).students
student_id3=collection.insert_one(thom).students
#print out data inserted
print("student records: ",student_id1,"",student_id2,"",student_id3)
