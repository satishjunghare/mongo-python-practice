import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["testdb"]

print(myclient.list_database_names())