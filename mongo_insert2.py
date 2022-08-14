import pymongo # mengimpor modul pymongo

# Konfigurasi mongodb
client = pymongo.MongoClient("mongodb+srv://masipnupro:Bismillah@cluster0.iubqgry.mongodb.net/?retryWrites=true&w=majority")

# Konfigurasi database
db = client['data_siswa']

# Konfigurasi koleksi
my_collections = db['jurusan_rpl']

# Data yang ingin dimasukkan
siswa_1 = {'nama':'Toni','Jurusan':'RPL','Nilai':90}
siswa_2 = {'nama':'Tini','Jurusan':'RPL','Nilai':80}
siswa_3 = {'nama':'Arin','Jurusan':'PBS','Nilai':75}
siswa_4 = {'nama':'Enzy','Jurusan':'PBS','Nilai':85}

results = my_collections.insert_many([siswa_1,siswa_2,siswa_3,siswa_4])

# Menghasilkan id data yang dimasukkan
print("Data berhasil ditambahkan")
print("Id data 1 = ", results.inserted_ids[0])
print("Id data 2 = ", results.inserted_ids[1])
print("Id data 3 = ", results.inserted_ids[2])
print("Id data 4 = ", results.inserted_ids[3])


# rec_id1 = my_collections.insert_one(siswa_1)
# rec_id2 = my_collections.insert_one(siswa_2)

# print("Data inserted with record ids",rec_id1," ",rec_id2)