from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

import search
import download

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/search', methods=['POST'])
def searchPage():
	return render_template('search.html')

@app.route('/parsing')
def parsing():
	global pathN
	pathN = str(request.args.get('path'))
	return search.search(request.args.get('path'))

@app.route("/download", methods=['post'])
def downloadPage():
	path = pathN
	fname = str(request.form.get('fname'))
	return download.download(path, fname)

if __name__ == '__main__':
	# app.debug = True
	app.run(host='0.0.0.0')