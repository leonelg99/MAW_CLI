import tkinter as tk
import threading
from connection import reciveMessages, obtener_ipv4
from interfaz import WINDOW, windowsGrid, windowInit
#from video import recivirImagen 
from joystick import joystickRead
import time
def receiveMsg():
    while True:
        reciveMessages()
        time.sleep(0.2)
    


def threads():
    incoming_message_thread = threading.Thread(target=receiveMsg)
    incoming_message_thread.daemon = True
    incoming_message_thread.start()
    #video_thread = threading.Thread(target=recivirImagen)
    #video_thread.daemon = True
    #video_thread.start()
    joystick_thread = threading.Thread(target=joystickRead)
    joystick_thread.daemon = True
    joystick_thread.start()

# Código principal
if __name__ == "__main__":
    SERVER_IP=obtener_ipv4()
    print(SERVER_IP)
    windowInit()
    windowsGrid()
    threads()
    WINDOW.mainloop()
