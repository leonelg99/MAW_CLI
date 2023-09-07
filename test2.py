import cv2
import tkinter as tk
import pygame
from pygame.locals import *
from PIL import Image, ImageTk 
# Configurar Pygame para el joystick
pygame.init()
pygame.joystick.init()

# Crear una ventana de Tkinter
root = tk.Tk()
root.title("Cámara y Joystick")

# Crear un lienzo para mostrar la cámara
canvas = tk.Canvas(root, width=640, height=480)
canvas.pack(side=tk.LEFT)

# Configurar la captura de video desde la cámara (ajusta el número de cámara según corresponda)
cap = cv2.VideoCapture(0)

# Función para mostrar la cámara en el lienzo
def mostrar_camara():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convertir de BGR a RGB
        img = Image.fromarray(frame)  # Convierte el cuadro en una imagen de Pillow
        img = ImageTk.PhotoImage(image=img)  # Convierte la imagen de Pillow en una PhotoImage
        canvas.create_image(0, 0, anchor=tk.NW, image=img)
        root.img = img  # Almacena la referencia a la imagen para evitar que sea recolectada por el recolector de basura
        root.after(10, mostrar_camara)  # Actualizar cada 10 milisegundos

mostrar_camara()  # Iniciar la visualización de la cámara

# Crear una etiqueta para mostrar los inputs del joystick
joystick_label = tk.Label(root, text="Inputs del Joystick:")
joystick_label.pack(side=tk.RIGHT)



# Función para mostrar los inputs del joystick
def mostrar_joystick():
    pygame.event.pump()  # Actualizar los eventos del joystick
    num_joysticks = pygame.joystick.get_count()
    if num_joysticks > 0:
        joystick = pygame.joystick.Joystick(0)  # Usar el primer joystick (índice 0)
        joystick.init()
        axes = joystick.get_numaxes()
        buttons = joystick.get_numbuttons()
        
        joystick_text = "Ejes:"
        for i in range(axes):
            joystick_text += f"\nAxis {i}: {joystick.get_axis(i):.2f}"
        
        joystick_text += "\n\nBotones:"
        for i in range(buttons):
            joystick_text += f"\nButton {i}: {joystick.get_button(i)}"
        
        joystick_label.config(text=joystick_text)
    
    root.after(100, mostrar_joystick)  # Actualizar cada 100 milisegundos

mostrar_joystick()  # Iniciar la visualización de los inputs del joystick

# Función para cerrar la ventana
def cerrar_ventana():
    cap.release()  # Liberar la captura de video
    root.quit()

root.protocol("WM_DELETE_WINDOW", cerrar_ventana)  # Configurar la acción al cerrar la ventana

# Iniciar la aplicación Tkinter
root.mainloop()
