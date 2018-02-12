import os
import json
import NTFSParsing
from flask import send_from_directory

def download(path, fname):
    return send_from_directory(path, fname)