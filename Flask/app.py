from flask import Flask,render_template,request,url_for,redirect,Response,stream_with_context
import cv2
import math
import json
import random
import time
import numpy as np
from keras.models import load_model
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return(redirect(url_for("login")))

@app.route('/Login' , methods=["POST","GET"])
def login():
    Usernames=['Rhys','Sai','Pranav','Kapil','Ralph',]
    Passwords=['123','123','123','123']
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
    

camera = cv2.VideoCapture(0)



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

@app.route('/Result')
def res():
    return classify(camera,'Classification Model\keras_model.h5','Classification Model\labels.txt')
    #return {'LABEL':f'Something','MAX':f'10','MIN':f'20'}


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

data=[]

@app.route('/Random')
def chart_data():
    
    def generate_random_data():  
        
        data.append(random.random()) 
        return json.dumps({'VALUE':random.random()})
           

    return generate_random_data()


def classify(img,modelFile,labels):
     # Load the model
        model = load_model(modelFile)

        camera = img

        labels = open(labels, 'r').readlines()
        

        

        ret, image = camera.read()
        image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
        image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
        image = (image / 127.5) - 1
        probabilities = model.predict(image)
        ret ={'LABEL':f'{labels[np.argmax(probabilities)]}','MAX':f'{np.max(probabilities)}','MIN':f'{np.min(probabilities)}'}
        json_dump=json.dumps(ret)
        return json_dump




