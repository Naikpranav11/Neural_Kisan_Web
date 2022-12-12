CamSrc=0
# camera = cv2.VideoCapture(CamSrc)



# def gen_frames():  
    
#     while True:
#         success, frame = camera.read()  # read the camera frame
#         if not success:
#             break
#         else:
#             ret, buffer = cv2.imencode('.jpg', (frame))
#             frame = buffer.tobytes()
            
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

