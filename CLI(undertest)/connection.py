import socket
import tkinter as tk
from tkinter import messagebox
import threading
from shared_variables import ESP32_CAM_IP, ESP32_CAM_PORT
from interfaz import WINDOW
import time
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
               