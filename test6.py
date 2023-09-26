import tkinter as tk
from PIL import Image, ImageTk

# Declarar una variable global para la imagen
imagen = None

def windowInit():
    global imagen  # Acceder a la variable global imagen
    # Configuro la ventana
    WINDOW = tk.Tk()
    WINDOW.title("MAW")
    WINDOW.resizable(1, 1)
    WINDOW.minsize(1280, 720)
    WINDOW.configure(bg="darkgrey")

    #Camera
    CAMERA_FRAME = tk.Frame(WINDOW, bg="blue")
    CAMERA_FRAME.grid(row=0,column=0, sticky="nsew",rowspan=WINDOW.grid_size()[1])
    CAMERA_FRAME.columnconfigure(0, weight=6)
    CAMERA_FRAME.rowconfigure(0, weight=1)
    # Crear un Frame para el logo
    LOGO_FRAME = tk.Frame(WINDOW, bg="red")
    LOGO_FRAME.grid(row=0, column=1, sticky="nsew")

    # Abrir la imagen y redimensionar
    img = Image.open("not_signal.jpg")
    img = img.resize((200, 200))

    # Crear una PhotoImage desde la imagen
    imagen = ImageTk.PhotoImage(img)

    # Crea un Label en LOGO_FRAME para mostrar la imagen
    LOGO_LABEL = tk.Label(LOGO_FRAME, image=imagen)
    LOGO_LABEL.grid(row=0, column=1, sticky="nsew")  # Establece sticky para ajustar la imagen al tamaño de la celda

    # Configurar la fila y columna para que se expandan correctamente
    LOGO_FRAME.columnconfigure(1, weight=4)
    LOGO_FRAME.rowconfigure(1, weight=1)

    return WINDOW

# Inicia el bucle principal de tkinter
WINDOW = windowInit()
WINDOW.mainloop()
