import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo de Organización")
ventana.resizable(1,1)
# Utilizando pack para organizar widgets verticalmente


# Utilizando grid para organizar widgets en una cuadrícula
etiqueta3 = tk.Label(ventana, text="Widget 3")
etiqueta3.grid(row=0, column=1)

etiqueta4 = tk.Label(ventana, text="Widget 4")
etiqueta4.grid(row=1, column=0, columnspan=2)


ventana.mainloop()
