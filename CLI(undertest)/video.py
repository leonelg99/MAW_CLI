from shared_variables import ESP32_CAM_IP, ESP32_CAM_PORT
from interfaz import update_camera
import cv2
from interfaz import add_message
from PIL import Image, ImageTk
from urllib.request import urlopen
import requests
import numpy as np
import os
import datetime
import time
import sys

url = 'http://192.168.4.1:8020'

def recivirImagen():
    CAMERA_BUFFRER_SIZE=4096
    stream=urlopen(url)
    bts=b''
    i=0
    while True:
        try:
            bts+=stream.read(CAMERA_BUFFRER_SIZE)
            jpghead=bts.find(b'\xff\xd8')
            jpgend=bts.find(b'\xff\xd9')
            if jpghead>-1 and jpgend>-1:
                jpg=bts[jpghead:jpgend+2]
                bts=bts[jpgend+2:]
                img=cv2.imdecode(np.frombuffer(jpg,dtype=np.uint8),cv2.IMREAD_UNCHANGED)
                img=cv2.resize(img,(760,630))
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(img)
                photo = ImageTk.PhotoImage(img)
                update_camera(photo)
            k=cv2.waitKey(1)
            #img=Image.fromarray(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
            #img.thumbnail((480,360))
            #imagen = ImageTk.PhotoImage(img)
            #WINDOW.CAMERA_LABEL.configure(image=imagen)
            #WINDOW.CAMERA_LABEL.image = imagen
            #CAMERA_LABEL.configure(image=imagen)
            #CAMERA_LABEL.image = imagen
            #if cv2.waitKey(1) == ord("q"):
                #break
        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud: {e}")
            bts=b''
            stream=urlopen(url)
            break
    cv2.destroyAllWindows()