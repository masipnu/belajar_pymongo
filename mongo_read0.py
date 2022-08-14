import pymongo # mengimpor modul pymongo

# Konfigurasi mongodb
client = pymongo.MongoClient("mongodb+srv://masipnupro:Bismillah@cluster0.iubqgry.mongodb.net/?retryWrites=true&w=majority")

# Konfigurasi database
db = client['data_siswa']

# Konfigurasi koleksi
my_collections = db['jurusan_rpl']

# Melakukan looping data
for x in my_collections.find():
	print(x)