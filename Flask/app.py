import json
import requests
from flask import Flask,render_template
from Functions.getData import APIJSON,Instructions

app=Flask(__name__)




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api')
def api():
    return APIJSON('https://scriptsapi.netlify.app/Scripts/test.json')


@app.route('/instructions/<param>/<cutoff>')
def apiSend(param,cutoff):
    return json.dumps(Instructions(param,int(cutoff)))