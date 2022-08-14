# Memasukkan library flask
from flask import Flask

# Membuat instance
app = Flask(__name__)

# Membuat rute
@app.route('/')
def index():
	return 'Halo kamu'

@app.route('/anisa')
def sapa_anisa():
	return 'Halo Anisa, tetep semangat ya :)'

@app.route('/radifka')
def sapa_radifka():
	return 'Halo Radifka, kamu lagi boring ya? ;)'

@app.route('/dini')
def sapa_dini():
	return 'Halo Dini, kamu bosen ya? :D'

@app.route('/suqya')
def sapa_suqya():
	return 'Halo Suqya, kamu bingung ya? :-( '

if __name__ == '__main__':
	app.run(debug=True)