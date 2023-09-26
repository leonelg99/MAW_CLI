import tkinter as tk
from PIL import Image, ImageTk


WINDOW = tk.Tk()
WINDOW.title("MAW")
WINDOW.resizable(1, 1)
WINDOW.minsize(1280, 720)
WINDOW.configure(bg="darkgrey")
WINDOW.columnconfigure(0, weight=6)
WINDOW.columnconfigure(1, weight=4)
WINDOW.rowconfigure(0, weight=3)
WINDOW.rowconfigure(1, weight=7)

FIRST_COLUMN_WIDGET = tk.Frame(WINDOW, bg="blue")
FIRST_COLUMN_WIDGET.grid(row=0, column=0, rowspan=2, sticky="nsew")
FIRST_COLUMN_WIDGET.columnconfigure(0, weight=6)

SECOND_COLUMN_WIDGET_1 = tk.Frame(WINDOW, bg="red")
SECOND_COLUMN_WIDGET_1.grid(row=0, column=1, rowspan=1, sticky="nsew")
SECOND_COLUMN_WIDGET_1.columnconfigure(0, weight=1)  # Configura el peso de la columna dentro de SECOND_COLUMN_WIDGET_1
SECOND_COLUMN_WIDGET_1.rowconfigure(0, weight=1)  # Configura el peso de la fila dentro de SECOND_COLUMN_WIDGET_1

img = Image.open("not_signal.jpg")
#img = img.resize((200, 200))
max_width = 200
max_height = 200
if img.width > max_width or img.height > max_height:
        img.thumbnail((max_width, max_height))
# Crear una PhotoImage desde la imagen
imagen = ImageTk.PhotoImage(img)
LOGO_LABEL = tk.Label(SECOND_COLUMN_WIDGET_1, image=imagen, anchor="center")
LOGO_LABEL.grid(row=0, column=0,sticky="nsew")  # Ajusta la imagen al tamaño del Frame SECOND_COLUMN_WIDGET_1


SECOND_COLUMN_WIDGET_2 = tk.Frame(WINDOW, bg="green")     
SECOND_COLUMN_WIDGET_2.grid(row=1, column=1, rowspan=2,sticky="nsew")
SECOND_COLUMN_WIDGET_2.columnconfigure(1, weight=4)
SECOND_COLUMN_WIDGET_2.rowconfigure(1, weight=7)
WINDOW.mainloop()
