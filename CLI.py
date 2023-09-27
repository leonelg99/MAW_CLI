import socket
import cv2
import tkinter as tk
from PIL import Image, ImageTk

def connectionInit():
    IP = "192.168.0.3"
    PORT = 80
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((IP, PORT))
        message = "Connection successful"
        client.sendall(message.encode())
        dat=client.recv(1024)
        print("Respuesta",dat)
    except Exception as e:
        print("Error al conectar: ",str(e))
    return client

def windowInit():
    # Configurar la ventana
    WINDOW = tk.Tk()
    WINDOW.title("MAW")
    WINDOW.resizable(1, 1)
    WINDOW.minsize(1280, 720)
    WINDOW.configure(bg="darkgrey")
    WINDOW.columnconfigure(0, weight=7)
    WINDOW.columnconfigure(1, weight=3)
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
    LOGO_LABEL = tk.Label(image=imagen, anchor="center")
    LOGO_LABEL.image = imagen  # Mantén una referencia a la imagen

    # Configurar el tamaño máximo para la columna y fila
    LOGO_LABEL.grid(row=0, column=1, sticky="nsew")
    LOGO_LABEL.grid_rowconfigure(0, weight=1)
    LOGO_LABEL.grid_columnconfigure(1, weight=1)

def windowsGrid():
    # Camera
    CAMERA_FRAME = tk.Frame(WINDOW, bg="blue")
    CAMERA_FRAME.grid(row=0, column=0, rowspan=2, sticky="nsew")
    CAMERA_FRAME.columnconfigure(0, weight=6)

    # Logo
    cargar_y_mostrar_imagen()

    # Terminal
    TERMINAL_FRAME = tk.Frame(WINDOW, bg="green")
    TERMINAL_FRAME.grid(row=1, column=1, rowspan=2, sticky="nsew")
    TERMINAL_FRAME.columnconfigure(1, weight=4)
    TERMINAL_FRAME.rowconfigure(1, weight=7)

# Código principal
if __name__ == "__main__":
    # Configuraciones iniciales y diseño de ventana
    #JOYSTICK = joystickInit()
    #cliente=connectionInit()
    #CAP = cv2.VideoCapture(0)
    WINDOW = windowInit()
    windowsGrid()

    WINDOW.mainloop()
