import os
import json
import NTFSParsing

def search(path):
	volume = path.split(":")[0] + ":"
	ntfsParsing = NTFSParsing.Extract_File(volume)
	data = ntfsParsing.open_directory(path.split(":\\")[1])

	return json.dumps(data)