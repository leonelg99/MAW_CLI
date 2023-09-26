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

    # Crear un Frame para el logo (60% de la pantalla)
    LOGO_FRAME = tk.Frame(WINDOW, bg="red")
    LOGO_FRAME.grid(row=0, column=0, rowspan=2, sticky="nsew")
    WINDOW.columnconfigure(0, weight=6)  # Configura la columna para ocupar el 60% de la pantalla

    # Abrir la imagen y redimensionar
    img = Image.open("not_signal.jpg")
    img = img.resize((200, 200))

    # Crear una PhotoImage desde la imagen
    imagen = ImageTk.PhotoImage(img)

    # Crea un Label en LOGO_FRAME para mostrar la imagen
    LOGO_LABEL = tk.Label(LOGO_FRAME, image=imagen)
    LOGO_LABEL.grid(row=0, column=1, sticky="nsew")  # Establece sticky para ajustar la imagen al tamaño de la celda

    # Configurar la fila y columna para que se expandan correctamente
    LOGO_FRAME.columnconfigure(0, weight=1)
    LOGO_FRAME.rowconfigure(0, weight=1)

    # Widget que ocupa toda la primera columna (60% de la pantalla)
    FIRST_COLUMN_WIDGET = tk.Frame(WINDOW, bg="blue")
    FIRST_COLUMN_WIDGET.grid(row=0, column=0, rowspan=2, sticky="nsew")

    # Segundo widget en la segunda columna (40% de la pantalla)
    SECOND_COLUMN_WIDGET = tk.Frame(WINDOW, bg="green")
    SECOND_COLUMN_WIDGET.grid(row=1, column=1, rowspan=2, sticky="nsew")
    WINDOW.columnconfigure(1, weight=4)  # Configura la columna para ocupar el 40% de la pantalla

    # Widget en la primera fila del segundo widget (35% de la columna)
    FIRST_ROW_SECOND_WIDGET = tk.Frame(SECOND_COLUMN_WIDGET, bg="orange")
    FIRST_ROW_SECOND_WIDGET.grid(row=0, column=0, sticky="nsew")
    SECOND_COLUMN_WIDGET.rowconfigure(0, weight=3)  # Configura la fila para ocupar el 35% superior de la columna

    # Widget en la segunda fila del segundo widget (65% de la columna)
    SECOND_ROW_SECOND_WIDGET = tk.Frame(SECOND_COLUMN_WIDGET, bg="purple")
    SECOND_ROW_SECOND_WIDGET.grid(row=1, column=0, sticky="nsew")
    SECOND_COLUMN_WIDGET.rowconfigure(1, weight=7)  # Configura la fila para ocupar el 65% inferior de la columna

    return WINDOW

# Inicia el bucle principal de tkinter
WINDOW = windowInit()
WINDOW.mainloop()
