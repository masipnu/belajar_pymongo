# Memasukkan library flask
from flask import Flask, request

# Membuat instance
app = Flask(__name__)

# Membuat rute
@app.route('/', methods=['GET','POST'])
def index():
	if request.method=='POST':
		return 'Kamu menggunakan method POST'
	elif request.method=='GET':
		return 'Kamu menggunakan method GET'

if __name__ == '__main__':
	app.run(debug=True)