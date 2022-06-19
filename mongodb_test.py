from pymongo import MongoClient
url="mongodb://admin:<password>@ac-opq9v6w-shard-00-00.e9lvado.mongodb.net:27017,ac-opq9v6w-shard-00-01.e9lvado.mongodb.net:27017,ac-opq9v6w-shard-00-02.e9lvado.mongodb.net:27017/?ssl=true&replicaSet=atlas-vi5co6-shard-0&authSource=admin&retryWrites=true&w=majority";
client=MongoClient(url)
db=client.pytech
print(db.list_collection_names())