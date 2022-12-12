from flask import Flask,render_template,request,url_for,redirect,Response,stream_with_context
# import cv2
from VideoProcessor import *
import math
import json
import random
import time
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from keras.models import load_model
import joblib
from DecisionMaker import *

#from keras.models import load_model
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return(redirect(url_for("login")))

@app.route('/Login' , methods=["POST","GET"])
def login():
    Usernames=['Rhys','Sai','Pranav','Kapil','Ralph',]
    Passwords=['123','123','123','123','123']
    if request.method == "POST":   
        Username=request.form['Username']
        Password=request.form['Password']

        for i in range(len(Usernames)):
            if(Username == Usernames[i] and Password==Passwords[i]): 
                return(redirect(url_for("Dash",Username=Username)))
        else:
          return render_template("login.html")
    return render_template('login.html')


@app.route('/Admin=<Username>')
def Dash(Username):
    return render_template('Dashboard.html',Username=Username)
    
@app.route('/Result')
def res():
   return classify(camera,'Classification Model\keras_model.h5','Classification Model\labels.txt')

@app.route('/ResultG')
def result():
    WaterLevel=round(random.random(),2)
    LightLevel=round(random.random(),2)
    if WaterLevel>0.5:
        WateringResult='Add Water'
    else:
        WateringResult='Dont Water'


    r=round(random.random()*255,2)
    g=round(random.random()*255,2)
    b=round(random.random()*255,2)
    a=round(random.random(),2)
    lightRGB=f'rgba({r},{g},{b},{a})'

    temperature=round(random.random()*30,2)

    if temperature>20:
        TempCommand='Cool'
    elif temperature<10:
        TempCommand='Warm'
    else:
        TempCommand='Normal'
    DiseaseList=['none','Aster Yellows','Bacterial Wilt','Blight','Canker','Crown Gall','Rot','Scab']
    cameraSource=CamSrc
    Disease=DiseaseList[random.randint(0,6)]

    return json.dumps({'Water':{'Sensor Water Level':f'{WaterLevel}','Watering Result':f'{WateringResult}'},'Light':{'Sensor Light Level':f'{LightLevel}','RGBA':f'{lightRGB}'},'Cooling':{'Temperature':f'{temperature}','Command':f'{TempCommand}'},'Camera':{'src':f'{cameraSource}','Disease':f'{Disease}'}})

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


##PRANAV ENTER CODE HERE
@app.route('/Decision')
def Decision_maker():
    dum=DM()
    dum.Train('iris.csv')
    return dum.Classify()



if __name__ == '__main__':
  app.run()
