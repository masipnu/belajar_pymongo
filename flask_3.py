# Memasukkan library flask
from flask import Flask, request

# mengimpor modul pymongo
import pymongo

# Konfigurasi mongodb
client = pymongo.MongoClient("mongodb+srv://masipnupro:Bismillah@cluster0.iubqgry.mongodb.net/?retryWrites=true&w=majority")

# Konfigurasi database
db = client['data_siswa']

# Konfigurasi koleksi
my_collections = db['jurusan_rpl']

# Membuat instance
app = Flask(__name__)

# Membuat rute
@app.route('/')
def index():
	for x in my_collections.find({"Jurusan":"RPL"}):
		return(x)

if __name__ == '__main__':
	app.run(debug=True)