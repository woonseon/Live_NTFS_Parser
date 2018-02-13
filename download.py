import os
import json
import NTFSParsing
from flask import send_from_directory

def download(path, fname):
    try:
        filePath = path + "/" + fname
        return send_file(filePath, as_attachment=True)
    except Exception as e:
        error = "Invalid File Name"