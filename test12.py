import tkinter as tk

def create_bordered_frame(parent_frame, border_color, inner_frame_options=None):
    # Crea el Frame interno
    inner_frame = tk.Frame(parent_frame, **(inner_frame_options or {}))
    inner_frame.pack(fill="both", expand=True)

    # Configura el color del borde
    inner_frame.configure(bg=border_color)

    # Crea el Frame principal (el contenedor)
    border_frame = tk.Frame(parent_frame)
    border_frame.pack(fill="both", expand=True)

    # Coloca el Frame interno dentro del Frame principal
    inner_frame.grid(row=0, column=0, sticky="nsew")

    return border_frame

# Crea la ventana principal
root = tk.Tk()
root.geometry("400x300")

# Crea un Frame con borde negro
bordered_frame = create_bordered_frame(root, "black", {"bg": "white"})
bordered_frame.pack(fill="both", expand=True)

# Agrega contenido al Frame interno
content_label = tk.Label(bordered_frame, text="Contenido del Frame", padx=20, pady=20)
content_label.pack(fill="both", expand=True)

root.mainloop()
