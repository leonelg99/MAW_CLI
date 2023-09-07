import cv2
import tkinter as tk
from PIL import Image, ImageTk
import pygame
from pygame.locals import *

# Configurar Pygame para el joystick
pygame.init()
pygame.joystick.init()

# Crear un diccionario para mapear números de botones a nombres reales
boton_mapping = {
    0: "1",
    1: "2",
    2: "3",
    3: "4",
    4: "L1",
    5: "R1",
    6: "L2",
    7: "R2",
    8: "Select",
    9: "Start",
    10: "Stick Izquierdo",
    11: "Stick Derecho",
}

# Crear una ventana de Tkinter
root = tk.Tk()
root.title("Cámara y Joystick")

# Crear un lienzo para mostrar la cámara
canvas = tk.Canvas(root, width=640, height=480)
canvas.grid(row=0, column=0, padx=10, pady=10)

# Configurar la captura de video desde la cámara (ajusta el número de cámara según corresponda)
cap = cv2.VideoCapture(0)

# Función para mostrar la cámara en el lienzo
def mostrar_camara():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        img = ImageTk.PhotoImage(image=img)
        canvas.create_image(0, 0, anchor=tk.NW, image=img)
        root.img = img
        root.after(10, mostrar_camara)

mostrar_camara()

# Crear un marco para la información del joystick
joystick_frame = tk.Frame(root)
joystick_frame.grid(row=0, column=1, padx=10, pady=10)

# Configurar la columna del marco del joystick para que tenga un tamaño fijo
root.grid_columnconfigure(1, minsize=200)

# Función para mostrar los inputs del joystick
def mostrar_joystick():
    joystick_text = "Inputs del Joystick:\n\n"
    pygame.event.pump()  # Actualizar los eventos del joystick
    num_joysticks = pygame.joystick.get_count()
    
    if num_joysticks > 0:
        joystick = pygame.joystick.Joystick(0)  # Usar el primer joystick (índice 0)
        joystick.init()
        
        axes = joystick.get_numaxes()
        buttons = joystick.get_numbuttons()
        
        # Mapear los nombres reales de los botones utilizando el diccionario
        for i in range(buttons):
            nombre_boton = boton_mapping.get(i, str(i))
            estado_boton = joystick.get_button(i)
            
            if nombre_boton in ["1", "2", "3", "4"]:
                # Representa los botones 1, 2, 3 y 4 con círculos rojos
                color = "red" if estado_boton else "white"
                canvas.create_oval(300, 300, 340, 340, outline="black", fill=color)
            
            joystick_text += f"{nombre_boton}: {estado_boton}\n"
        
        joystick_text += "\n\nStick Derecho:"
        if joystick.get_axis(3) < 0:
            joystick_text += f"\nArriba: {joystick.get_axis(3):.2f}"
        elif joystick.get_axis(3) > 0:
            joystick_text += f"\nAbajo: {joystick.get_axis(3):.2f}"
        if joystick.get_axis(2) < 0:
            joystick_text += f"\nIzquierda: {joystick.get_axis(2):.2f}"
        elif joystick.get_axis(2) > 0:
            joystick_text += f"\nDerecha: {joystick.get_axis(2):.2f}"
        if joystick.get_axis(3) == 0 and joystick.get_axis(2) == 0:
            joystick_text += f"\nNO MOVE"

        joystick_text += "\n\nStick Izquierdo:"
        if joystick.get_axis(1) < 0:
            joystick_text += f"\nArriva: {joystick.get_axis(1):.2f}"
        elif joystick.get_axis(1) > 0:
            joystick_text += f"\nAbajo: {joystick.get_axis(1):.2f}"
        if joystick.get_axis(0) < 0:
            joystick_text += f"\nIzquierda: {joystick.get_axis(0):.2f}"
        elif joystick.get_axis(0) > 0:
            joystick_text += f"\nDerecha: {joystick.get_axis(0):.2f}"
        if joystick.get_axis(1) == 0 and joystick.get_axis(0) == 0:
            joystick_text += f"\n NO MOVE\n"
        
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
