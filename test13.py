import pygame
import time

def joystickInit():
    pygame.init()
    pygame.joystick.init()
    joystick_count = pygame.joystick.get_count()
    
    if joystick_count == 0:
        print("No se ha encontrado ningún joystick.")
        return None

    # Selecciona el primer joystick (índice 0)
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    return joystick

def main():
    joystick = joystickInit()

    if joystick:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN:
                    button = event.button
                    print(f"Botón presionado: {button}")
                elif event.type == pygame.JOYAXISMOTION:
                    axis = event.axis
                    value = round(event.value * 100)
                    print(f"Eje {axis}: {value}%")
            time.sleep(0.2)

if __name__ == "__main__":
    main()
