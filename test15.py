import pygame
import math
def read_joystick_axes():
    pygame.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    while True:
        pygame.event.pump()
        x_axis = joystick.get_axis(0)
        y_axis = joystick.get_axis(1)

        # Calcula el ángulo en radianes
        radians = math.atan2(-y_axis, x_axis)

        # Convierte el ángulo a grados y asegúrate de que sea positivo
        degrees = math.degrees(radians)
        if degrees < 0:
            degrees += 360

        print(f"Ángulo: {degrees:.2f} grados")

if __name__ == "__main__":
    read_joystick_axes()