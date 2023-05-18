from flask import Flask, redirect, url_for, jsonify
from markupsafe import escape
from flask import request
import requests

app = Flask(__name__)

@app.route("/login")
def login():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    p = requests.get('https://jsonplaceholder.typicode.com/posts/1',headers=headers)
    return p.json()

#Rest API Verbs - GET, POST, PUT, DELETE
#List, dict --> jsonify() --> json - data representation

#angular, react, vue, vanilla js.

#API - Application Programming Interface
