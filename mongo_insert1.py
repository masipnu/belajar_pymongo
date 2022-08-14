import pymongo # mengimpor modul pymongo

# Konfigurasi mongodb
client = pymongo.MongoClient("mongodb+srv://masipnupro:Bismillah@cluster0.iubqgry.mongodb.net/?retryWrites=true&w=majority")

# Konfigurasi database
db = client['data_siswa']

# Konfigurasi koleksi
my_collections = db['jurusan_rpl']

# Data yang ingin dimasukkan
siswa = {'nama':'Anisa','Jurusan':'RPL','Nilai':95}

results = my_collections.insert_one(siswa)

# Menghasilkan id data yang dimasukkan
print("Data berhasil ditambahkan dengan Id = ", results.inserted_id)