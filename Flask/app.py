import json
import requests
import random
from flask import Flask,render_template
from Functions.getData import APIJSON,Instructions
from Functions.NN_Classify import Classify

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



@app.route('/Classified/<i>')
def Cl(i):
    # 'img_1.jpg'
    return str(Classify(i))

@app.route('/output')
def Output():
    Instr=Instructions('temperature',random.randint(0,200))
    if(Instr!='Do Nothing'):
        highlight='highlight'
    else:
        highlight=''
    return json.dumps({'message':Instr,'option':highlight})