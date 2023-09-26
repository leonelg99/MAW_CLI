import tkinter as tk

def obtener_dimensiones_ventana():
    # Inicializa la ventana tkinter
    ventana = tk.Tk()

    # Establece el tamaño mínimo de la ventana
    ventana.minsize(640, 480)

    # Muestra el ancho y alto de la ventana
    ancho_ventana = ventana.winfo_width()
    alto_ventana = ventana.winfo_height()

    # Cierra la ventana tkinter
    ventana.destroy()

    return ancho_ventana, alto_ventana

# Obtiene las dimensiones de la ventana
ancho, alto = obtener_dimensiones_ventana()

# Muestra las dimensiones en la consola
print("Ancho de la ventana:", ancho)
print("Alto de la ventana:", alto)
