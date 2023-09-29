import socket
import tkinter as tk
from tkinter import messagebox
import threading
from shared_variables import ESP32_CAM_IP, ESP32_CAM_PORT
from interfaz import WINDOW,add_message
import time
import sys
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
            message = "Connection successful\n"
            add_message(message,"success")
            client.sendall(message.encode())
            dat=client.recv(1024).decode()
            add_message("Respuesta {dat}","process")
            connection_event.set()
            break
        except Exception as e:
            trys+=1
            print("Error al conectar: ",str(e))
            add_message("Error al conectar: "+str(e),"error")
            if(trys>=5):
                show_error_message()
            else:
                retry = retry_connection()
                if(retry==False):
                   WINDOW.destroy()
                   sys.exit()
                else:
                    time.sleep(0.5)    
    incoming_message_thread = threading.Thread(target=recivirMensajes)
    incoming_message_thread.daemon = True
    incoming_message_thread.start()      


def connectionClose():
    connection_event.clear()
    client.close()
    add_message("Conexión cerrada","error")
    time.sleep(1)
    WINDOW.destroy()
    sys.exit()

def sendCommand(command):
    try:
        client.sendall(command.encode())
        add_message(command,"process")
    except Exception as e:
        add_message("Error al enviar comando: "+str(e),"error")
        connectionClose()

def recivirMensajes():
    while True:
        try:
            data = client.recv(1024)
            if data:
                add_message(data.decode(),"incoming")
        except Exception as e:
            add_message("Error al recibir datos: "+str(e),"error")
            #connectionClose()
        time.sleep(1)
    