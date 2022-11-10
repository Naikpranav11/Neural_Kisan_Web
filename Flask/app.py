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
    return Response(classify(camera,'Classification Model\keras_model.h5','Classification Model\labels.txt'),mimetype='text/plain')


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

data=[]

@app.route('/chart_data')
def chart_data():
    
    def generate_random_data():  
        while True:
            data.append(random.random()) 
            yield f'{random.random()},\n'
            time.sleep(1)
           

    return Response(generate_random_data(),mimetype='text/plain')


def classify(img,modelFile,labels):
     # Load the model
        model = load_model(modelFile)

        camera = img

        labels = open(labels, 'r').readlines()
        while True:

        

            ret, image = camera.read()
            image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
            image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
            image = (image / 127.5) - 1
            probabilities = model.predict(image)

            yield f'{labels[np.argmax(probabilities)]}'




