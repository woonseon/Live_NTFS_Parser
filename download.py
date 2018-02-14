import os
import json
import NTFSParsing
from flask import send_from_directory

def download(path, fname):
    try:
        return send_from_directory(path, fname)

    except Exception as e:
        error = "Invalid File Name"