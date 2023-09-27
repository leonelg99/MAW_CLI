import tkinter as tk
from PIL import Image, ImageTk

WINDOW = tk.Tk()

def windowInit():
    # Configurar la ventana
    #WINDOW = tk.Tk()
    WINDOW.title("MAW")
    WINDOW.resizable(1, 1)
    WINDOW.minsize(1280, 720)
    WINDOW.configure(bg="darkgrey")
    WINDOW.columnconfigure(0, weight=6)
    WINDOW.columnconfigure(1, weight=4)
    WINDOW.rowconfigure(0, weight=2)
    WINDOW.rowconfigure(1, weight=8)


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
    TERNMINAL_EVENTS = tk.Frame(TERMINAL_FRAME, bg="black",border=1, borderwidth=1)
    TERNMINAL_EVENTS.grid(row=1, column=1, sticky="nsew")

    #Area terminal
    global TERMINAL_TEXT
    TERMINAL_TEXT = tk.Text(TERNMINAL_EVENTS, bg="black", fg="white", font=("Consolas", 12),  wrap=tk.WORD)
    TERMINAL_TEXT.grid(row=0, column=0, sticky="nsew")

    # Scrollbar
    
    TERMINAL_SCROLLBAR = tk.Scrollbar(TERNMINAL_EVENTS, command=TERMINAL_TEXT.yview)
    TERMINAL_SCROLLBAR.grid(row=0, column=1, sticky="nsew")
    TERMINAL_TEXT["yscrollcommand"] = TERMINAL_SCROLLBAR.set

def add_message(message):
    TERMINAL_TEXT.insert(tk.END, message + "\n")
    TERMINAL_TEXT.see(tk.END)