import socket
import cv2
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import sys
import threading
import time
import pygame

ESP32_CAM_IP = "-"
ESP32_CAM_PORT = 80

connection_event = threading.Event()

def show_error_message():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal de tkinter
    messagebox.showerror("Error de conexión", "No se pudo establecer la conexión después de 5 intentos.")

def retry_connection():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal de tkinter
    return messagebox.askyesno("Reintentar conexión", "¿Deseas intentar la conexión nuevamente?")
  

def connectionInit():   
    global client
    client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    trys=0
    while (trys<5):
        try:
            client.connect((ESP32_CAM_IP, ESP32_CAM_PORT))
            message = "Connection successful"
            client.sendall(message.encode())
            dat=client.recv(1024)
            print("Respuesta",dat)
            connection_event.set()
            break
        except Exception as e:
            trys+=1
            print("Error al conectar: ",str(e))
            if(trys>=5):
                show_error_message()
            else:
                retry = retry_connection()
                if(retry==False):
                   WINDOW.destroy()
                   sys.exit()
                else:
                    time.sleep(0.5)          
                   

                
        

def windowInit():
    # Configurar la ventana
    WINDOW = tk.Tk()
    WINDOW.title("MAW")
    WINDOW.resizable(1, 1)
    WINDOW.minsize(1280, 720)
    WINDOW.configure(bg="darkgrey")
    WINDOW.columnconfigure(0, weight=6)
    WINDOW.columnconfigure(1, weight=4)
    WINDOW.rowconfigure(0, weight=2)
    WINDOW.rowconfigure(1, weight=8)
    return WINDOW

def cargar_y_mostrar_imagen():
    img = Image.open("LOGO.png")
    max_width = 280
    max_height = 216
    img.thumbnail((max_width, max_height))
    # Crear una PhotoImage desde la imagen
    imagen = ImageTk.PhotoImage(img)
    LOGO_LABEL = tk.Label(image=imagen, anchor="center", bg="darkgrey")
    LOGO_LABEL.image = imagen  # Mantén una referencia a la imagen

    # Configurar el tamaño máximo para la columna y fila
    LOGO_LABEL.grid(row=0, column=1, sticky="nsew")
    LOGO_LABEL.grid_rowconfigure(0, weight=1)
    LOGO_LABEL.grid_columnconfigure(1, weight=1)

def windowsGrid():
    # Camera
   

    img=Image.open("not_signal.jpg")
    #img.thumbnail((768,432))
    #img.resize((68,20))
    imagen=ImageTk.PhotoImage(img)
    CAMERA_LABEL = tk.Label(image=imagen,width=768, height=432, anchor="center")
    CAMERA_LABEL.image = imagen  # Mantén una referencia a la imagen
    CAMERA_LABEL.grid(row=0, column=0,rowspan=2, sticky="nsew")
 
   
    # Logo
    cargar_y_mostrar_imagen()

    # Terminal
    TERMINAL_FRAME = tk.Frame(WINDOW, bg="darkgrey")
    TERMINAL_FRAME.grid(row=1, column=1, rowspan=2, sticky="nsew")
    TERMINAL_FRAME.columnconfigure(1, weight=4)
    TERMINAL_FRAME.rowconfigure(1, weight=7)
    TERMINAL_LABEL = tk.Label(TERMINAL_FRAME, text="Event Monitor", bg="#E65D0E", fg="black", anchor="center", font=("Verdana", 20, "bold"))
    TERMINAL_LABEL.grid(row=0, column=0, sticky="nsew",columnspan=2)
    TERMINAL_LABEL.grid_columnconfigure(0, weight=1)
    TERMINAL_LABEL.grid_rowconfigure(0, weight=1)
    TERNMIL_EVENTS = tk.Frame(TERMINAL_FRAME, bg="black",border=1, borderwidth=1)
    TERNMIL_EVENTS.grid(row=1, column=1, sticky="nsew")



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
        if cv2.waitKey(1) == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()

def joystickInit():
    pygame.init()# Inicializar el joystick
    pygame.joystick.init()
    while(pygame.joystick.get_count()==0):
        print("Conecte un joystick")
        time.sleep(2)
    joystick = pygame.joystick.Joystick(0)  # Selecciona el primer joystick
    joystick.init()
    return joystick

def joystickRead():
    joystick = joystickInit()

   

def main():
    #wifi_thread = threading.Thread(target=connectionInit)
    #wifi_thread.daemon = True
    #wifi_thread.start()  
    video_thread = threading.Thread(target=recivirImagen)
    video_thread.daemon = True
    video_thread.start()
    joystick_thread = threading.Thread(target=joystickRead)
    joystick_thread.daemon = True
    joystick_thread.start()


# Código principal
if __name__ == "__main__":
    # Configuraciones iniciales y diseño de ventana
    #JOYSTICK = joystickInit()
    #cliente=connectionInit()
    #CAP = cv2.VideoCapture(0)
    WINDOW = windowInit()
    windowsGrid()
    main()
    WINDOW.mainloop()
