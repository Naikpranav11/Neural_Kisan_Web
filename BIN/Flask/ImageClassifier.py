import cv2,json
import numpy as np
from keras.models import load_model

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