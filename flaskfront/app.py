from flask import Flask, render_template, jsonify, request
import json
import requests
import Scnr
import os

studyguide = Scnr.Scnr()

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/test')

def test():
    message = {'greeting':'Hello from Flask!'}
    return jsonify(message)  # serialize and use JSON headers

@app.route('/add', methods = ['POST'])
def addURL():

    data = json.loads(request.data)
    url_to_add = data['url']
    studyguide.add_url(url_to_add)
    # studyguide.to_pdf()

    # result = request.form;
    # msg = {'greeting':"test"}
    # print(request.form["url"])
    # studyguide.add_url(url)
    msg = {'greeting':studyguide.count}
    return jsonify(msg)

@app.route('/gen', methods = ['GET'])
def generatePDF():
    studyguide.to_pdf()