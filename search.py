import os
import json
import NTFSParsing
from flask import render_template

def search(path):
	try:
		volume = path.split(":")[0] + ":"
		ntfsParsing = NTFSParsing.Extract_File(volume)
		data = ntfsParsing.open_directory(path.split(":\\")[1])

		return json.dumps(data)
	except:
		return "none"