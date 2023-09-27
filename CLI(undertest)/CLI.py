
import tkinter as tk
import threading
from connection import connectionInit
from interfaz import WINDOW, windowsGrid, windowInit
from video import recivirImagen 
from joystick import joystickRead
def main():
    #wifi_thread = threading.Thread(target=connectionInit)
    #wifi_thread.daemon = True
    #wifi_thread.start()  
    #video_thread = threading.Thread(target=recivirImagen)
    #video_thread.daemon = True
    #video_thread.start()
    joystick_thread = threading.Thread(target=joystickRead)
    joystick_thread.daemon = True
    joystick_thread.start()

# Código principal
if __name__ == "__main__":
    #joystickRead()
    windowInit()
    windowsGrid()
    main()
    WINDOW.mainloop()
