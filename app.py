from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

import search

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/search', methods=['POST'])
def searchPage():
	return render_template('search.html')

@app.route('/parsing')
def parsing():
	return search.search(request.args.get('path'))

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')