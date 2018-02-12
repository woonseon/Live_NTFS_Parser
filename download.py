import os
import json
import NTFSParsing
from flask import send_from_directory

def download(path, fname):
    print(path)
    print(fname)
    return send_from_directory('C:\\Users\dbdns\Downloads', '다운로드.png')