from shared_variables import ESP32_CAM_IP, ESP32_CAM_PORT
from interfaz import WINDOW
from connection import connection_event, connectionClose
import cv2
from PIL import Image, ImageTk


def recivirImagen():
    connection_event.wait()
    cap = cv2.VideoCapture(f"rtsp://{ESP32_CAM_IP}:{ESP32_CAM_PORT}/")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error al recibir imagen")
            break
        #cv2.imshow("Frame", frame)
        img=Image.fromarray(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
        img.thumbnail((480,360))
        imagen = ImageTk.PhotoImage(img)
        WINDOW.CAMERA_LABEL.configure(image=imagen)
        WINDOW.CAMERA_LABEL.image = imagen
        #CAMERA_LABEL.configure(image=imagen)
        #CAMERA_LABEL.image = imagen
        #if cv2.waitKey(1) == ord("q"):
            #break
    cap.release()
    cv2.destroyAllWindows()
    connectionClose()