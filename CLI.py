# Importa los módulos necesarios
import socket
import pygame
import cv2
import tkinter as tk
from PIL import Image, ImageTk

def windowInit():
    #Configuro la ventana
    WINDOW = tk.Tk()
    WINDOW.title("MAW")
    WINDOW.resizable(1,1)
    WINDOW.minsize(1280,720)
    WINDOW.configure(bg="darkgrey")
    WINDOW.columnconfigure(0, weight=6)
    WINDOW.columnconfigure(1, weight=4)
    WINDOW.rowconfigure(0, weight=3)
    WINDOW.rowconfigure(1, weight=7)
    return WINDOW

def joystickInit():
    #Configuro el joystick
    pygame.init()
    pygame.joystick.init()
    if pygame.joystick.get_count() == 0:
        print("No se ha detectado ningún joystick")
        return False
    else: 
          joystick = pygame.joystick.Joystick(0)
          joystick.init() 
    return joystick

def cargar_y_mostrar_imagen(LOGO_FRAME):
    img = Image.open("LOGO.png")
    max_width = 512
    max_height = 216
    img = img.resize((max_width, max_height))
    print()
    # Crear una PhotoImage desde la imagen
    imagen = ImageTk.PhotoImage(img)
    LOGO_LABEL = tk.Label(LOGO_FRAME, image=imagen, anchor="center")
    LOGO_LABEL.image = imagen  # Mantén una referencia a la imagen
    LOGO_LABEL.grid(row=0, column=0,sticky="nsew")


def windowsGrid():

    #Camera
    CAMERA_FRAME = tk.Frame(WINDOW, bg="blue")
    CAMERA_FRAME.grid(row=0, column=0, rowspan=2, sticky="nsew")
    CAMERA_FRAME.columnconfigure(0, weight=6)

    #Logo
    LOGO_FRAME = tk.Frame(WINDOW, bg="red")
    LOGO_FRAME.grid(row=0, column=1, rowspan=1, sticky="nsew")
    LOGO_FRAME.columnconfigure(0, weight=1)
    LOGO_FRAME.rowconfigure(0, weight=1)
    cargar_y_mostrar_imagen(LOGO_FRAME)
    #Terminal
    TERMINAL_FRAME = tk.Frame(WINDOW, bg="green")
    TERMINAL_FRAME.grid(row=1, column=1, rowspan=2,sticky="nsew")
    TERMINAL_FRAME.columnconfigure(1, weight=4)
    TERMINAL_FRAME.rowconfigure(1, weight=7)



# Código principal
if __name__ == "__main__":
    
    #Configuracion
    # Configurar Pygame para el joystick
    JOYSTICK = joystickInit()
    # Configurar CV2 para la cámara
    CAP = cv2.VideoCapture(0)
    # Configurar Tkinter para la ventana
    WINDOW=windowInit()
    #Diseño de ventana

    windowsGrid()

    WINDOW.mainloop()
