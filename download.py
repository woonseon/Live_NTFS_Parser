import os
import json
import NTFSParsing
from flask import send_from_directory
from flask import render_template

def download(path, fname):
    try:
        return send_from_directory(path, fname)

    except ValueError:
        return "none"