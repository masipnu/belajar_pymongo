import pymongo # mengimpor modul pymongo

# Konfigurasi mongodb
client = pymongo.MongoClient("mongodb+srv://masipnupro:Bismillah@cluster0.iubqgry.mongodb.net/?retryWrites=true&w=majority")
db = client.test

# Menampilkan deskripsi database
print(db)