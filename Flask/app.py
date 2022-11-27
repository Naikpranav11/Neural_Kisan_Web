from flask import Flask,render_template,request,url_for,redirect,Response,stream_with_context
import cv2
import math
import json
import random
import time
import numpy as np
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
    
CamSrc=0
camera = cv2.VideoCapture(CamSrc)



def gen_frames():  
    
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', (frame))
            frame = buffer.tobytes()
            
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

#@app.route('/Result')
#def res():
#    return classify(camera,'Classification Model\keras_model.h5','Classification Model\labels.txt')

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

data=[]


##PRANAV ENTER CODE HERE
@app.route('/Decision')
def Decision_maker():
    
    return json.dumps()

##PRANAV ENTER CODE HERE

#def classify(img,modelFile,labels):
     # Load the model
#        model = load_model(modelFile)
#
#        camera = img
#
#        labels = open(labels, 'r').readlines()
#        
#
#        
#
#        ret, image = camera.read()
#        image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
#        image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
#        image = (image / 127.5) - 1
#        probabilities = model.predict(image)
#        ret ={'LABEL':f'{labels[np.argmax(probabilities)]}','MAX':f'{np.max(probabilities)}','MIN':f'{np.min(probabilities)}'}
#        json_dump=json.dumps(ret)
#        return json_dump




