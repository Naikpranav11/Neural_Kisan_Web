from flask import Flask,render_template,request,url_for,redirect,Response,stream_with_context
import cv2
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

data=[]



class DM:
    def __init__():
        return 0
    def Train(self,csvPath):
        df = pd.read_csv(csvPath)

        iris = datasets.load_iris()

        import pandas as pd
        data=pd.DataFrame({
        'sepal length':iris.data[:,0],
        'sepal width':iris.data[:,1],
        'petal length':iris.data[:,2],
        'petal width':iris.data[:,3],
        'species':iris.target
            })
        data.head()


        X=data[['sepal length', 'sepal width', 'petal length', 'petal width']]  # Features
        y=data['species']  # Labels

        # Split dataset into training set and test set
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3) # 70% training and 30% test
        from sklearn.ensemble import RandomForestClassifier
        
        #Create a Gaussian Classifier
        clf=RandomForestClassifier(n_estimators=100)

        #Train the model using the training sets y_pred=clf.predict(X_test)
        clf.fit(X_train,y_train)

        
        print('Trained')
        # joblib.dump(clf,'model.pkl')
        # print("Model Saved")
    def Classify(self):
        # lr=joblib.load('model.pkl')
        y_pred= self.clf.predict(self.X_test)
        species_idx = self.clf.predict([[3, 5, 4, 2]])[0]
        return self.iris.target_names[species_idx]


##PRANAV ENTER CODE HERE
@app.route('/Decision')
def Decision_maker(csvPath):
    
    dum=DM()
    dum.Train('iris.csv')
    

    return dum.Classify()

##PRANAV ENTER CODE HERE

def classify(img,modelFile,labels):
     ##Load the model
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




