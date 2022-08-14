from flask import Flask,request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def entry_point():
	return 'Ini halaman index'

@app.route('/test', methods=['GET','POST'])
def halaman_test():
	print ('Kamu sedang membuka halaman test')
	if request.method == 'GET':
		return 'dengan metode GET'
	elif request.method == 'POST':
		return 'dengan metode POST '
	
if __name__ == '__main__':
	app.run(debug=True)