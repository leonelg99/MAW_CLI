import pygame
import time
from interfaz import add_message
from conecctionv2 import sendMessage
#KEYS:
#0: 1
#1: 2
#2: 3
#3: 4
#4: L1
#5: R1
#6: L2
#7: R2
#8: Select
#9: Start
#10: Stick Izquierdo
#11: Stick Derecho
### STICK DERECHO
#### A3: Arriva: de 0.0 a -1.0
####     Abajo: de 0.0 a 1.0
#### A2: Izquierda: de 0.0 a -1.0
####     Derecha: de 0.0 a 1.0
### STICK IZQUIERDO 
#### A1: Arriva: de 0.0 a -1.0
####     Abajo: de 0.0 a 1.0
#### A0: Izquierda: de 0.0 a -1.0
####     Derecha: de 0.0 a 1.0

KEY_MAPS = {
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
    11: "Stick Derecho"
}

def joystickInit():
    pygame.init()# Inicializar el joystick
    pygame.joystick.init()
    
    while(pygame.joystick.get_count()<=0):
        add_message("Conecte un joystick","warning")
        time.sleep(2)

    joystick = pygame.joystick.Joystick(0)  # Selecciona el primer joystick
    joystick.init()
    return joystick

def joystickRead():
    joystick=joystickInit()
    if joystick:
        while True:
            try:
                for event in pygame.event.get():
                    if event.type == pygame.JOYBUTTONDOWN:
                        button = event.button
                        #print(f"Botón presionado: {button}")
                        add_message(KEY_MAPS[button], "normal")
                        sendMessage(KEY_MAPS[button],0)
                    elif event.type == pygame.JOYAXISMOTION:
                        axis = event.axis
                        value = round((event.value)*100)
                        data = f"A{axis}:{value}"
                        add_message(data, "normal")
                        message = f"{value}A{axis}"
                        #print(f"Eje {axis}: {value}%")
            except KeyboardInterrupt:
                pass
            time.sleep(0.6)
    
