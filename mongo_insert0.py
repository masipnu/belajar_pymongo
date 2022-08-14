import pymongo

myclient = pymongo.MongoClient("mongodb+srv://masipnupro:Bismillah@cluster0.iubqgry.mongodb.net/?retryWrites=true&w=majority")
mydb = myclient["data_siswa"]
mycol = mydb["jurusan_rpl"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)

print(x.inserted_id)